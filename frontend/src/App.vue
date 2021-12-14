<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title>
        <v-btn link to="/">Notes list</v-btn>
      </v-toolbar-title>
    </v-app-bar>
    <v-main>
      <v-container>
        <v-row>
          <v-col cols="12" sm="3">

          </v-col>
          <v-col cols="12" sm="6">
            <v-card rounded="lg" elevation="3">
              <v-container>
                <router-view/>
              </v-container>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<style lang="scss">

</style>
<script>
export default {
  mounted() {
    this.$vuetify.theme.dark = true
  }
}
</script>
