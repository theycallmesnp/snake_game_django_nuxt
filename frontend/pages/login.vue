<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Login</button>
      <div v-if="error" style="color:red">{{ error }}</div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()

const login = async () => {
  try {
    const data = await $fetch('http://127.0.0.1:8000/api/auth/login/', {
      method: 'POST',
      body: { email: email.value, password: password.value }
    })
    localStorage.setItem('token', data.token)
    router.push('/snake')
  } catch (e) {
    error.value = 'Invalid credentials'
  }
}
</script> 