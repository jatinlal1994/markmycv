<template>
  <div id="auth-first-step" :class="status">
    <div class="short-description">
      <p>Access our features</p>
    </div>
    <div class="long-description">
      <p>Please enter the Username you used to sign up on our Website to access all the features including templates, services and support. Note that username is of atleast 4 characters and is unique.</p>
    </div>
    <div class="auth-input-field" :class="username.field_class">
      <input type="text" v-model="username.value" @input="refreshUsernameError" @focus="refreshUsernameError" :class="username.input_class" spellcheck="false" placeholder="Username" />
      <div class="field-status"><div v-if="username.is_valid"><i class="fas fa-check"></i></div><div v-else><i class="fas fa-times"></i></div></div>
    </div>
    <div class="first-step-next">
      <div class="input-email-submit">
        <div class="continue-loading" v-if="form_loading"><Loading /></div>
        <p v-else class="submit-email" @click="submitUsername">Next <i class="fas fa-chevron-right"></i></p>
      </div>
      <div class="form-error" v-if="form_error"><p v-text="username_error"></p></div>
      <div class="start-signup" v-if="username.value == '' && form_error == ''"><p @click="createAccount">Create Account</p></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UsernameStep',
  data () {
    return {
      username: { value: '', field_class: '', input_class: '', is_valid: '' },
      form_loading: '',
      form_error: ''
    }
  },
  props: {
    status: String
  },
  methods: {
    submitUsername () {
      // let data = this.$data
    },
    refreshUsernameError () {
      let username = this.$data.username
      // let formloading = this.$data.form_loading
      if (username.value === '') {
        setTimeout(function () { username.is_valid = false }, 250)
      } else if ((username.value.length > 0 && username.value.length <= 3) || !/^[a-zA-Z0-9]+$/.test(username.value)) {
        username.is_valid = false
      } else {
        username.is_valid = true
      }
      this.$data.form_error = ''
      username.field_class = (username.value === '') ? '' : 'filled'
    },
    createAccount () {
      this.$emit('closeAuthModal')
    }
  }
}
</script>

<style lang="scss">
  .start-signup{margin-top: 10px;float: left;
    p{display: inline;font-size: 11px;font-weight: 600;border-radius: 4px;padding: 5px 5px;cursor: pointer;transition: 150ms;color: #1ABC9C;text-shadow: 0px 0px 1px rgba(0,0,0,0.15);
      i{margin-right: 2px;transition: 150ms;}
      &:hover{color: #16A085;}
    }
  }
  .first-step-next{
    .input-email-submit{float: right;}
    .form-error{float: left;margin-top: 10px;line-height: 25px;padding: 0 3px;}
    &:after{clear: both;display: block;content: "";}
  }
</style>
