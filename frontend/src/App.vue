<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import NavbarComponentVue from './components/NavbarComponent.vue'

</script>

<template>
  <header>
    <NavbarComponentVue/>
    <RouterView/>

  </header>

</template>

<style scoped>

</style>
