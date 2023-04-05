<template>
  <div class="home">
    <Nav @login="login_username" @closeHome="closeHome" ref="nav" />
  </div>
</template>

<script>
import Nav from '@/components/Nav'

export default {
  name: 'home',
  components: {
    Nav
  },
  data () {
    return {
      background_status: '', overlay_class: '', login_username: '', is_logged_in: false, main_string: 'Stunning', main_string_class: '', to_width: 0
    }
  },
  metaInfo: {
    title: 'Create a stunning CV for your dream job',
    titleTemplate: 'MarkMyCV - %s',
    htmlAttrs: {
      lang: 'en',
      amp: true
    }
  },
  created () {
    let data = this.$data
    let userLoggedIn = window.localStorage.getItem('username')
    if (userLoggedIn !== '' && userLoggedIn !== null) {
      data.is_logged_in = true
    } else {
      data.is_logged_in = false
    }
    let counter = 0
    const strings = ['Stunning', 'Attractive', 'Simple', 'Professional']
    setInterval(function () {
      if (counter < strings.length - 1) {
        counter = counter + 1
      } else {
        counter = 0
      }
      data.to_width = 'width: 0px'
      setTimeout(function () {
        data.main_string = strings[counter]
        setTimeout(function () {
          data.to_width = 'width: ' + document.getElementById('main-string-inner').getBoundingClientRect().width + 'px'
        }, 500)
      }, 500)
    }, 5000)
  },
  methods: {
    closeHome (value) {
      let data = this.$data
      data.background_status = value
      if (value === 'opened') {
        data.overlay_class = 'opening'
        setTimeout(function () {
          data.overlay_class = 'opened'
        }, 10)
      } else {
        data.overlay_class = 'opening'
        setTimeout(function () {
          data.overlay_class = ''
        }, 500)
      }
    },
    proceedToTemplates () {
      let data = this.$data
      let userLoggedIn = window.localStorage.getItem('username')
      if (userLoggedIn !== '' && userLoggedIn !== null) {
        this.$router.push('/templates')
      } else {
        this.$refs.nav.openAuthModal()
        data.is_logged_in = false
      }
    }
  }
}
</script>

<style lang="scss">
</style>
