<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="username" type="text" placeholder="Username" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <input v-model="phone" type="text" placeholder="Phone" />
      <button type="submit">Register</button>
      <div v-if="error" style="color:red">{{ error }}</div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('')
const username = ref('')
const password = ref('')
const phone = ref('')
const error = ref('')
const router = useRouter()

const register = async () => {
  try {
    await $fetch('http://127.0.0.1:8000/api/auth/register/', {
      method: 'POST',
      body: {
        email: email.value,
        username: username.value,
        password: password.value,
        phone_number: phone.value
      }
    })
    router.push('/login')
  } catch (e) {
    error.value = 'Registration failed'
  }
}
</script> 