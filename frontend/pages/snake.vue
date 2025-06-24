<template>
  <div>
    <h2>Snake Game</h2>
    <canvas
      ref="canvas"
      width="400"
      height="400"
      style="border: 1px solid #000"
    ></canvas>
    <div v-if="gameOver">
      <h3>Game Over! Your score: {{ score }}</h3>
      <button @click="startGame">Play Again</button>
    </div>
    <div v-else>
      <h3>Score: {{ score }}</h3>
    </div>
    <button @click="fetchScores" style="margin-top: 20px">
      Show My Scores
    </button>
    <ul>
      <li v-for="score in scores" :key="score.id">
        {{ score.score }} - {{ new Date(score.date_played).toLocaleString() }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const canvas = ref(null);
const ctx = ref(null);
const box = 20;
const score = ref(0);
const gameOver = ref(false);
const direction = ref("RIGHT");
const snake = ref([]);
const food = ref({ x: 0, y: 0 });
const scores = ref([]);

const randomPosition = () => ({
  x: Math.floor(Math.random() * 20) * box,
  y: Math.floor(Math.random() * 20) * box,
});

const draw = () => {
  ctx.value.clearRect(0, 0, 400, 400);
  // Draw snake
  ctx.value.fillStyle = "green";
  snake.value.forEach((part) => ctx.value.fillRect(part.x, part.y, box, box));
  // Draw food
  ctx.value.fillStyle = "red";
  ctx.value.fillRect(food.value.x, food.value.y, box, box);
};

const move = () => {
  if (gameOver.value) return;
  let head = { ...snake.value[0] };
  if (direction.value === "LEFT") head.x -= box;
  if (direction.value === "UP") head.y -= box;
  if (direction.value === "RIGHT") head.x += box;
  if (direction.value === "DOWN") head.y += box;

  // Check collision
  if (
    head.x < 0 ||
    head.x >= 400 ||
    head.y < 0 ||
    head.y >= 400 ||
    snake.value.some((part) => part.x === head.x && part.y === head.y)
  ) {
    gameOver.value = true;
    submitScore();
    return;
  }

  snake.value.unshift(head);
  if (head.x === food.value.x && head.y === food.value.y) {
    score.value++;
    food.value = randomPosition();
  } else {
    snake.value.pop();
  }
  draw();
};

const keyDownHandler = (e) => {
  if (e.key === "ArrowLeft" && direction.value !== "RIGHT")
    direction.value = "LEFT";
  if (e.key === "ArrowUp" && direction.value !== "DOWN") direction.value = "UP";
  if (e.key === "ArrowRight" && direction.value !== "LEFT")
    direction.value = "RIGHT";
  if (e.key === "ArrowDown" && direction.value !== "UP")
    direction.value = "DOWN";
};

let interval = null;
const startGame = () => {
  score.value = 0;
  direction.value = "RIGHT";
  snake.value = [{ x: 200, y: 200 }];
  food.value = randomPosition();
  gameOver.value = false;
  draw();
  if (interval) clearInterval(interval);
  interval = setInterval(move, 200);
};

const submitScore = async () => {
  const token = localStorage.getItem("token");
  console.log('Token used for submitScore:', token);
  if (!token) return;
  try {
    await $fetch("http://127.0.0.1:8000/api/snake/scores/", {
      method: "POST",
      body: { score: score.value },
      headers: { Authorization: `Token ${token}` },
    });
    fetchScores();
  } catch (e) {
    // ignore
  }
};

const fetchScores = async () => {
  const token = localStorage.getItem("token");
  console.log('Token used for fetchScores:', token);
  if (!token) return alert("Please login first!");
  try {
    const data = await $fetch("http://127.0.0.1:8000/api/snake/scores/", {
      headers: { Authorization: `Token ${token}` },
    });
    console.log(data, ":dldldldldldlddld--->");

    scores.value = data;
  } catch (e) {
    alert("Failed to fetch scores");
  }
};

onMounted(() => {
  ctx.value = canvas.value.getContext("2d");
  window.addEventListener("keydown", keyDownHandler);
  startGame();
});
</script> 