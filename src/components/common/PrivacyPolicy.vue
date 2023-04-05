<template>
  <div>
    <div id="terms-of-use" :class="computedStatus">
      <div class="modal-vertical">
        <div class="modal-container">
          <div class="modal-box">
            <div class="close-modal" @click="closeModal"><i class="fas fa-times"></i></div>
            <div class="modal-title"><p>Privacy Policy</p></div>
            <div class="terms-body" v-html="terms"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
#terms-of-use .modal-vertical .modal-container .modal-box{max-height: 400px;overflow-y: auto;min-height: 350px;}
#terms-of-use{
  .modal-title{border-bottom: 1px solid #eee;}
}
.terms-body{padding: 5px 15px;position: absolute;top: 40px;left: 0px;width: 100%;height: calc(100% - 40px);overflow-y: auto;box-sizing: border-box;
  .title{font-size: 13px;margin-bottom: 4px;margin-top: 3px;font-weight: 500;}
  .content{font-size: 11px;margin-bottom: 10px;}
  h1{font-size: 14px;text-align: center;}
  address{display: inline-block;font-family: "Poppins", sans-serif;border: 1px solid #ddd;font-style: normal;font-size: 11px;font-weight: 500;padding: 8px 12px;border-radius: 4px;background-color: #f6f6f6;margin: 3px 6px 15px 6px;color: #7F8C8D;}
  .content-desc{font-size: 11px;font-weight: 500;color: #16A085;margin-left: 4px;}
  ol{padding-left: 25px;font-size: 11px;
    li{list-style-type: decimal;margin-top: 5px;}
    ol{margin-top: 4px;
      li{list-style-type: disc;}
    }
  }
}
</style>

<script>
import axios from 'axios'

export default {
  name: 'PrivacyPolicy',
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
    axios.get('https://api.markmycv.com/api/privacy-policy')
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
    closeModal () { this.$emit('closePrivacyPolicy') }
  }
}
</script>
