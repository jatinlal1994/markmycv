<template>
  <div>
    <div id="auth-modal" :class="computedStatus">
      <div class="modal-vertical">
        <div class="modal-container">
          <div class="modal-box">
            <div class="close-modal" @click="closeModal"><i class="fas fa-times"></i></div>
            <div class="row">
              <div class="col intro-col">
                <div class="content">
                  <div class="logo"><p>markmycv.com</p></div>
                  <div class="tilt-brand"><p>MarkMyCV</p></div>
                  <div class="forgot-password"><p>Forgot Password ?</p></div>
                </div>
              </div>
              <div class="col image-col"></div>
              <div class="col fields-col">
                <div class="fields-inner">
                  <div class="logo"><i class="far fa-file-alt"></i></div>
                  <UsernameStep :status="username_step_status" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
#auth-modal{
  .modal-vertical{
    .modal-container{width: 700px;max-width: 700px;height: 400px;box-sizing: border-box;position: relative;
      .modal-box{position: absolute;top: 0;left: 0;width: 100%;height: 100%;padding: 0;overflow: hidden;box-shadow: 0 8px 17px 2px rgba(0,0,0,0.14), 0 3px 14px 2px rgba(0,0,0,0.12), 0 5px 5px -3px rgba(0,0,0,0.2);
        .row{height: 100%;}
        .col{position: absolute;height: 100%;}
      }
    }
  }
}
.intro-col{width: 25%;left: 0;
  .content{padding: 20px 0;box-sizing: border-box;
    .logo{text-align: center;
      p{font-size: 12px;font-weight: 600;color: #3d3d3d;}
    }
    .tilt-brand{position: absolute;left: -20px;top: 165px;
      p{font-size: 32px;transform: rotate(270deg);color: #aaa;}
    }
    .social-icons{position: absolute;bottom: 25px;width: 100%;text-align: center;
      .social-icons-row{width: 100%;
        .social-icons-col{display: inline-block;margin-right: 10px;
          i{font-size: 22px;vertical-align: middle;color: #3d3d3d;}
          &:last-child{margin-right: 0px;}
        }
        &:after{clear: both;display: block;content: "";}
      }
    }
    .forgot-password{position: absolute;bottom: 25px;width: 100%;text-align: center;
      i{margin-right: 1px;}
      p{font-size: 11px;font-weight: 600;cursor: pointer;display: inline-block;}
    }
  }
}
.image-col{width: 32%;left: 25%;background: url('../../images/auth-banner.jpg');background-size: cover;background-position: center;}
.fields-col{width: 43%;left: 57%;padding: 25px 35px;box-sizing: border-box;
  .fields-inner{padding: 12px 0;}
  .logo{padding-top: 14px;
    i{font-size: 20px;color: #2C3E50;}
  }
  .logo{margin-bottom: 38px;
    i{color: #3d3d3d;}
  }
  .short-description{position: relative;
    p{font-size: 17px;font-weight: 500;}
    &:after{display: block;content: "";margin-top: 6px;left: 0;width: 40px;height: 3px;background-color: #777;}
  }
  .long-description{margin-top: 18px;padding: 0 2px;width: 80%;
    p{font-size: 10px;font-weight: 500;color: #808e9b;}
  }
  .input-field{width: 88%;margin: 4px auto 6px auto;
    input{float: left;width: calc(100% - 32px);border-right: 0;border-radius: 4px 0 0 4px;text-align: left;}
    .submit-button{width: 32px;float: left;box-sizing: border-box;background-color: #3d3d3d;text-align: center;border-radius: 0 4px 4px 0;
      .sk-circle{margin: 8px auto;}
      i{line-height: 32px;color: #f6f6f6;font-size: 14px;display: block;}
    }
    &.error{
      input{border-color: #E74C3C;}
      .submit-button{background-color: #E74C3C;}
    }
    &.shaking{animation: shake 0.5s;animation-iteration-count: infinite;}
    &:after{clear: both;display: block;content: "";}
  }
  /*input{width: 100%;height: 32px;background-color: #eee;padding: 0 10px;box-sizing: border-box;border-radius: 4px;font-size: 12px;text-align: center;font-weight: 600;background-color: #fff;border: 1.5px solid #3d3d3d;
    &.error{border: 1.5px solid #E74C3C;color: #E74C3C}
    &.filled + .field-status{transform: translateX(20px);}
    &[readonly]{background: #2ECC71;color: #fff;}
  }*/
  .auth-input-field{margin-top: 20px;position: relative;
    input{width: 80%;height: 32px;background-color: #eee;padding: 0 10px;box-sizing: border-box;border-radius: 4px;font-size: 12px;font-weight: 600;background-color: #fff;border: 1.5px solid #3d3d3d;
      &.error{border: 1.5px solid #E74C3C;color: #E74C3C}
      &.filled + .field-status{transform: translateX(20px);}
      &[readonly]{background: #2ECC71;color: #fff;}
    }
    .field-status{position: absolute;top: 2px;z-index: -1;left: calc(80% - 12px);transform: translateX(0px);transition: 250ms;
      i{font-size: 12px;}
      .fa-check{color: #27AE60;}
      .fa-times{color: #C0392B;}
    }
    &.shaking{animation: shake 0.5s;animation-iteration-count: infinite;}
  }
  .input-email-submit, .register-submit{text-align: right;padding-right: 20%;margin-top: 10px;
    p{color: #eee;background-color: #3d3d3d;display: inline;font-size: 11px;font-weight: 600;border-radius: 4px;padding: 5px 10px;cursor: pointer;transition: 150ms;
      i{margin-left: 2px;}
      &:hover{background-color: lighten(#3d3d3d, 8%);}
    }
  }
}
</style>

<script>
import UsernameStep from './UsernameStep'

export default {
  name: 'AuthModal',
  props: { status: String },
  data () {
    return {
      username_step_status: ''
    }
  },
  computed: {
    computedStatus: function () { return 'modal ' + this.$props.status }
  },
  components: {
    UsernameStep
  },
  methods: {
    closeModal () {
      this.$emit('closeAuthModal')
    }
  }
}
</script>
