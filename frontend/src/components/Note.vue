<template>
  <v-card>
    <v-card-text>
      <v-row>
        <v-col>
          <v-switch inset label="Done" color="success" v-model="note.done"/>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-text-field dense hide-details label="Title" v-model="note.title"/>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-textarea dense hide-details label="Text" v-model="note.text"/>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn color="success" v-if="isEdit" @click="saveNote">Save</v-btn>
          <v-btn color="success" v-else @click="addNote">Add</v-btn>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>

export default {
  name: "NoteInfo",
  props: {
    note: {
      type: Object,
      required: true,
    },
    isEdit: {
      type: Boolean,
      default: false,
    }
  },
  methods: {
    addNote() {
      this.$emit('add', this.note)
    },
    saveNote() {
      this.$emit('save', this.note)
    }
  }
}
</script>

<style scoped>

</style>
