<template>
  <div class="home">
    <h1>Todo w/ Django & Vue</h1>
    <hr>
    <TodoInput @createTodoEvent="createTodo" />
    <TodoList :todos="todos"/>
  </div>
</template>

<script>
// @ is an alias to /src
import TodoList from '@/components/TodoList.vue'
import TodoInput from '@/components/TodoInput.vue'
import router from '@/router'
import jwtDecode from 'jwt-decode'
import axios from 'axios'

export default {
  name: 'home',
  data () {
    return {
      todos: [
        // {id:1, title:'Django DRF로 로그인 구현'},
        // {id:2, title:'JWT 활용한 세션 구현'},
        // {id:3, title:'Todo 관련 API 구현'},
        // {id:4, title:'Vuex 활용한 Flux 아키텍쳐 적용'},
      ]
    }
  },
  components: {
    TodoList, 
    TodoInput
  },
  methods: {
    loggedIn() {
      this.$session.start()

      if (!this.$session.has('jwt')) {
        router.push('/login')
      }
    },

    // 이 함수는 페이지가 load될 때마다 불려져야 한다. ()
    getTodos() {
      const token = this.$session.get('jwt')
      const user_id = jwtDecode(token).user_id // decode 후 user_id만 가져온다. 
      const options = {
        headers: {
          Authorization: 'JWT ' + token // JWT(공백)(토큰)
        }
      }
      // axios -> api/v1/users/{현재 접속한 유저의 id}
      axios.get(`http://localhost:8000/api/v1/users/${user_id}/`, options)
      .then(res => {
        // console.log(res.data.todo_set)
        this.todos = res.data.todo_set
      })
    },

    createTodo(title) {
      const token = this.$session.get('jwt')
      const user_id = jwtDecode(token).user_id // decode 후 user_id만 가져온다. 
      const options = {
        headers: {
          Authorization: 'JWT ' + token // JWT(공백)(토큰)
        }
      }
      const data = new FormData() // data 객체를 안전하게 만들어주는 클래스
      data.append('user', user_id) // append(key value)
      data.append('title', title)
      axios.post("http://localhost:8000/api/v1/todos/", data, options)
      .then(res => {
        this.todos.push(res.data)
      })
    },
  },

  // 8가지 life cycle hook
  mounted() {
    this.loggedIn()
    this.getTodos()
  }
}
</script>
