<template>
  <Note :note="note" is-edit
        @save="saveNote"
  />
</template>

<script>
import Note from '@/components/Note'
import axios from 'axios'

export default {
  name: "NoteDetail",
  components: {Note},
  mounted() {
    this.getNoteDetail()
  },
  data: () => ({
    note: {},
  }),
  methods: {
    async getNoteDetail() {
      const {data} = await axios.get(`http://localhost:8000/api/note/${this.$route.params.id}`)
      this.note = data
    },
    async saveNote() {
      await axios.put(`http://localhost:8000/api/note/${this.note.id}/`, this.note)
      this.$toast.success('Saved successful')
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>

</style>
