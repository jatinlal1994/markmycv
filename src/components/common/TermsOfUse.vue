<template>
  <div>
    <div id="terms-of-use" :class="computedStatus">
      <div class="modal-vertical">
        <div class="modal-container">
          <div class="modal-box">
            <div class="close-modal" @click="closeModal"><i class="fas fa-times"></i></div>
            <div class="modal-title"><p>Terms of Use</p></div>
            <div class="terms-body" v-html="terms"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
#terms-of-use .modal-vertical .modal-container .modal-box{max-height: 400px;overflow-y: auto;min-height: 350px;}
.terms-body{padding: 5px 15px;position: absolute;top: 40px;left: 0px;width: 100%;height: calc(100% - 40px);overflow-y: auto;box-sizing: border-box;
  .title{font-size: 13px;margin-bottom: 4px;margin-top: 3px;font-weight: 500;}
  .content{font-size: 11px;margin-bottom: 10px;}
}
</style>

<script>
import axios from 'axios'

export default {
  name: 'TermsOfUse',
  props: { status: String },
  data () {
    return {
      terms: ''
    }
  },
  computed: {
    computedStatus: function () { return 'modal ' + this.$props.status }
  },
  created () {
    let container = this
    axios.get('https://api.markmycv.com/api/terms-of-use')
      .then(function (response) {
        container.$data.terms = response.data.html
      })
      .catch(function (error) {
        console.log(error)
      })
      .finally(function () {
        // always executed
      })
  },
  methods: {
    closeModal () { this.$emit('closeTermsOfUse') }
  }
}
</script>
