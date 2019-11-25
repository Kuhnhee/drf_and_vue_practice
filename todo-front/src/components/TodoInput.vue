<template>
  <div class="todo-input">
    <h2>todo입력하기</h2>
    <form @submit.prevent="createTodo">
      <input v-model="title" type="text" class="form-control">
      <button type="submit" class="btn btn-primary">+</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'TodoInput',
  data() {
    return {
      title: ''
    }
  },
  methods: {
    createTodo() {
      this.$emit('createTodoEvent', this.title)
      this.title = '' //input form 초기화
    }
  }
}
</script>

<style>

</style>