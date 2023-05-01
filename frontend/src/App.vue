<script setup>
import { RouterView } from 'vue-router'
import NavbarComponentVue from './components/NavbarComponent.vue'

</script>

<template>
  <header>
    <NavbarComponentVue/>
    <main>
    <RouterView/>
  </main>
  </header>
</template>

<style scoped>
main{
  top: 20px;
  width: 100%;
}

</style>
