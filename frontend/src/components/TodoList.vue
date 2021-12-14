<template>
  <div>
    <v-card elevation="3">
      <v-btn fab left absolute small top link to="/note/add" color="success">
        <v-icon>mdi-plus</v-icon>
      </v-btn>
      <v-card-text>
        <v-list dense>
          <v-list-item v-for="note in notes" :key="note.id">
            <v-list-item-action>
              <v-switch color="success" readonly disabled v-model="note.done"/>
            </v-list-item-action>
            <v-list-item-content>
              <v-btn text link :to="`/note/${note.id}`">{{ note.title }}</v-btn>
            </v-list-item-content>
            <v-list-item-icon>
              <v-btn icon @click="deleteNote(note)">
                <v-icon color="error">mdi-delete</v-icon>
              </v-btn>
            </v-list-item-icon>
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'TodoList',
  mounted() {
    this.getNotes()
  },
  data: () => ({
    notes: [],
  }),
  methods: {
    async deleteNote(note) {
      if (confirm(`U rly want to delete ${note.title} note?`)) {
        await axios.delete(`http://localhost:8000/api/note/${note.id}/`)
        this.$toast.success('Successful deleted')
        this.getNotes()
      }
    },
    async getNotes() {
      const {data} = await axios.get('http://localhost:8000/api/note')
      this.notes = data
    }
  }
}
</script>
