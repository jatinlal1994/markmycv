<template>
  <div>
    <div id="settings" :class="computedStatus">
      <div class="modal-vertical">
        <div class="modal-container">
          <div class="modal-box">
            <div class="close-modal" @click="closeModal"><i class="fas fa-times"></i></div>
            <div class="modal-title"><p>Account Settings</p></div>
            <div class="settings-list">
              <ul>
                <!--<li>
                  <p>Registered Email ID</p>
                  <p>jatinlal1994@gmail.com</p>
                </li>-->
                <li>
                  <p>Mail me recommended jobs</p>
                  <div class="check-switch"><input type="checkbox" id="privacy-authentication"><label for="privacy-authentication"></label></div>
                </li>
                <li>
                  <p>Allow Companies to view your Resume</p>
                  <div class="check-switch"><input type="checkbox" id="check1"><label for="check1"></label></div>
                </li>
                <li>
                  <p>Use my details to suggest personalised jobs</p>
                  <div class="check-switch"><input type="checkbox" id="check1"><label for="check1"></label></div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.check-switch{float: right;}
.settings-list{
  li{padding: 10px 14px;border-bottom: 1px solid #eee;
    p{line-height: 14px;font-size: 11px;font-weight: 500;float: left;color: #34495E;
      &:first-child{font-weight: bold;}
      &:last-child{float: right;}
    }
    &:last-child{border-bottom: none;}
    &:after{clear: both;display: block;content: "";}
  }
}
</style>

<script>
export default {
  name: 'Settings',
  props: { status: String },
  computed: {
    computedStatus: function () { return 'modal ' + this.$props.status }
  },
  methods: {
    closeModal () { this.$emit('closePrivacySettings') }
  }
}
</script>
