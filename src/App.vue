<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <h1>Machine Learning Prototype</h1>
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/asder0815/VueML"
        target="_blank"
        text
      >
        <span class="mr-2">GitHub Repostory</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <MLMain/>
    </v-main>
  </v-app>
</template>

<script>
import MLMain from './components/MLMain';

export default {
  name: 'App',

  components: {
    MLMain,
  },

  data: () => ({
    //
  }),
};
</script>
