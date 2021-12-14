<template>
  <note :note="note"
        @add="addNote"
  />
</template>

<script>
import Note from '@/components/Note'
import axios from 'axios'
export default {
  name: "AddNote",
  components: {Note},
  data: () => ({
    note: {
      title: null,
      text: null,
    },
  }),
  methods: {
    async addNote() {
      await axios.post(`http://localhost:8000/api/note/`, this.note)
      this.$toast.success('Note successful added')
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>

</style>
