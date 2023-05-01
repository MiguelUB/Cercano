<template>
  <v-card max-width="448" class="mx-auto" color="grey-lighten-3">
    <v-layout>
      <v-app-bar color="teal-darken-4" image="https://picsum.photos/1920/1080?random">
        <template v-slot:image>
          <v-img gradient="to top right, rgba(255, 174, 71,.8), rgba(255, 240, 0,.8)"></v-img>
        </template>

        <div class="d-flex flex-row align-center">
          <v-img :width="50" src="src\assets\logo-removed.png"></v-img>
          <p>Cercano</p>
        </div>

        <v-spacer></v-spacer>

        <v-btn icon>
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>
      </v-app-bar>


    </v-layout>
  </v-card>
</template>

<script>

</script>