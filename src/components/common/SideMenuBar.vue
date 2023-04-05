<template>
  <div>
    <div id="side-menu-bar" :class="status">
      <div id="close-side-menu" @click="closeSideBar">
        <i class="fas fa-times"></i>
      </div>
      <div id="side-logo-bar">
        <router-link to="/">
          <p>MarkMyCV</p>
        </router-link>
      </div>
      <div v-if="logged" id="cover-profile">
        <div class="edit-profile" @click="openProfileModal">
          <p><i class="fas fa-pen"></i>Edit Profile</p>
        </div>
        <div class="cover-image"></div>
        <div class="profile-image">
          <img :src="profile_picture">
        </div>
        <div class="name">
          <p class="fullname">{{ fullname }}</p>
          <p class="email">{{ emailid }}</p>
        </div>
      </div>
      <ul id="side-menu-list">
        <li v-if="logged" @click="openProfileModal">
          <div class="left"><i class="fas fa-user"></i><p>My Profile</p></div>
          <div class="right"><i class="fas fa-chevron-right"></i></div>
        </li>
        <li @click="openTermsOfUse">
          <div class="left"><i class="fas fa-file-alt"></i><p>Terms of Use</p></div>
          <div class="right"><i class="fas fa-chevron-right"></i></div>
        </li>
        <li @click="openPrivacyPolicy">
          <div class="left"><i class="fas fa-user-shield"></i><p>Privacy Policy</p></div>
          <div class="right"><i class="fas fa-chevron-right"></i></div>
        </li>
        <!--<li @click="openTermsOfUse">
          <div class="left"><i class="fas fa-exclamation-triangle"></i><p>Disclaimer</p></div>
          <div class="right"><i class="fas fa-chevron-right"></i></div>
        </li>
        <li v-if="logged" @click="openPrivacySettings">
          <div class="left"><i class="fas fa-cog"></i><p>Account Settings</p></div>
          <div class="right"><i class="fas fa-chevron-right"></i></div>
        </li>-->
      </ul>
      <div class="login-request" v-if="!logged">
        <p>Please <span>login</span> to access more features of our website. You can use your Email ID to login to our website.</p>
      </div>
      <div v-if="logged" @click="logout" id="logout-button">
        <p>Logout</p><i class="fas fa-sign-out-alt"></i>
      </div>
    </div>
    <!--<Settings :status="privacyModalStatus" @closePrivacySettings="closePrivacySettings" />-->
    <TermsOfUse :status="termsOfUseStatus" @closeTermsOfUse="closeTermsOfUse" />
    <PrivacyPolicy :status="privacyPolicyStatus" @closePrivacyPolicy="closePrivacyPolicy" />
    <Profile @closeProfileModal="closeProfileModal" @profile="profile" :status="profileStatus" />
  </div>
</template>

<style lang="scss">
#side-menu-bar{position: fixed;top: 0px;left: 0;width: 280px;z-index: 5;box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.15);transition: 500ms ease transform;left: 0;height: 100vh;background-color: #fff;transform: translateX(0px);
  #logout-button{position: absolute;bottom: 0;left: 0;width: 100%;background-color: #E74C3C;text-align: center;padding: 0 15px;box-sizing: border-box;cursor: pointer;transition: 150ms;
    i{float: right;}
    p{float: left;}
    p, i{line-height: 42px;font-size: 12px;font-weight: 600;color: #f6f6f6;}
    &:hover{background-color: #C0392B;}
    &:after{clear: both;display: block;content: "";}
  }
  #close-side-menu{position: absolute;right: -28px;top: 10px;cursor: pointer;
    i{color: #333;font-size: 20px;}
  }
  #side-logo-bar{text-align: center;
    p{font-family: 'Barcelony', sans-serif;font-weight: bold;font-size: 14px;color: #f6f6f6;line-height: 44px;background-color: #333;}
  }
  #cover-profile{
    .edit-profile{position: absolute;right: 12px;top: 56px;background-color: rgba(0,0,0,0.3);border-radius: 4px;padding: 5px 10px;cursor: pointer;transition: 250ms;
      i{margin-right: 4px;}
      p{font-size: 11px;font-weight: 600;color: #f6f6f6;
        i{font-size: 0.9em;margin-right: 6px;}
      }
      &:hover{background-color: rgba(0,0,0,0.5);}
    }
    .cover-image{background-color: #1abc9c;background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120' viewBox='0 0 120 120'%3E%3Cpolygon fill='%23000000' fill-opacity='.1' points='120 0 120 60 90 30 60 0 0 0 0 0 60 60 0 120 60 120 90 90 120 60 120 0'/%3E%3C/svg%3E");width: 100%;height: 120px;background-size: 34px;box-shadow: inset 0 0 10px 0 rgba(0,0,0,0.5);}
    .profile-image{margin-top: -50px;width: 100%;margin-left: 10px;
      img{width: 100px;height: 100px;display: block;border-radius: 50%;box-shadow: 0 2px 5px 0 rgba(0,0,0,0.2);}
    }
    .name{text-align: left;margin: -44px 0 25px 116px;
      p{
        &.fullname{font-size: 14px;font-weight: 700;}
        &.email{font-size: 11px;font-weight: 700;color: #7F8C8D;font-family: "Barlow", sans-serif;margin-left: 1px;}
      }
    }
  }
  #side-menu-list{}
  li{padding: 0 12px;transition: 150ms;cursor: pointer;padding-right: 10px;transition: 150ms;
    .left{float: left;
      i{margin-right: 7px;}
    }
    .right{float: right;}
    i{font-size: 13px;}
    p{font-size: 12px;font-weight: bold;}
    i, p{display: inline;line-height: 42px;color: #333;}
    &:hover{background-color: #1ABC9C;
      i, p{color: #fff;}
    }
    &:after{clear: both;display: block;content: "";}
    &:hover{padding-right: 8px;}
    &:last-child{border-bottom: 0;}
  }
  .login-request{padding: 10px 12px;position: absolute;bottom: 0;left: 0;
    p{font-size: 11px;font-weight: 600;color: #7F8C8D;
      span{color: #16A085;}
    }
  }
  &.closed{transform: translateX(-280px);
    #close-side-menu{opacity: 0;display: none;}
  }
  &.opened{top: translateX(0px);
    #close-side-menu{opacity: 1;display: block;}
  }
}
.check-switch{float: right;
  input{display: none;
    & + label{width: 28px;height: 14px;background-color: #ddd;border-radius: 10px;display: block;position: relative;cursor: pointer;transition: 250ms;box-shadow: inset 0 0 4px 0 rgba(0,0,0,0.15);
      &:after{width: 10px;height: 10px;content: "";display: block;background-color: #fff;box-sizing: border-box;position: absolute;top: 2px;border-radius: 50%;left: 3px;transition: 250ms;transform: translateX(0px);box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.3);}
    }
    &:checked + label{background-color: #2ECC71;}
    &:checked + label:after{transform: translateX(12px);background-color: #fff;}
    }
  }
</style>

<script>
// import Settings from '@/components/common/Settings'
import TermsOfUse from '@/components/common/TermsOfUse'
import PrivacyPolicy from '@/components/common/PrivacyPolicy'
import Profile from '@/components/common/Profile'

export default {
  name: 'SideMenuBar',
  props: { status: String, logged: Boolean, username: String },
  data () {
    return {
      privacyModalStatus: 'closed',
      termsOfUseStatus: 'closed',
      profileStatus: 'closed',
      privacyPolicyStatus: 'closed',
      picture: '',
      fullname: '',
      emailid: ''
    }
  },
  computed: {
    profile_picture: function () {
      let data = this.$data
      if (data.picture === '') {
        return ''
      } else {
        return 'https://api.markmycv.com//api/image/' + this.$data.picture
      }
    }
  },
  components: { TermsOfUse, PrivacyPolicy, Profile },
  methods: {
    openPrivacySettings: function () {
      let status = this.$data
      this.$emit('clicked')
      status.privacyModalStatus = 'opening'
      setTimeout(function () {
        status.privacyModalStatus = 'opened'
      }, 10)
    },
    openProfileModal: function () {
      let status = this.$data
      this.$emit('clicked')
      status.profileStatus = 'opening'
      setTimeout(function () {
        status.profileStatus = 'opened'
      }, 10)
    },
    closePrivacySettings: function () {
      let status = this.$data
      status.privacyModalStatus = 'opening'
      setTimeout(function () {
        status.privacyModalStatus = 'closed'
      }, 500)
    },
    closeProfileModal () {
      let status = this.$data
      status.profileStatus = 'opening'
      setTimeout(function () {
        status.profileStatus = 'closed'
      }, 500)
    },
    openTermsOfUse: function () {
      let status = this.$data
      this.$emit('clicked')
      status.termsOfUseStatus = 'opening'
      setTimeout(function () {
        status.termsOfUseStatus = 'opened'
      }, 10)
    },
    closeTermsOfUse: function () {
      let status = this.$data
      status.termsOfUseStatus = 'opening'
      setTimeout(function () {
        status.termsOfUseStatus = 'closed'
      }, 500)
    },
    openPrivacyPolicy: function () {
      let status = this.$data
      this.$emit('clicked')
      status.privacyPolicyStatus = 'opening'
      setTimeout(function () {
        status.privacyPolicyStatus = 'opened'
      }, 10)
    },
    closePrivacyPolicy: function () {
      let status = this.$data
      status.privacyPolicyStatus = 'opening'
      setTimeout(function () {
        status.privacyPolicyStatus = 'closed'
      }, 500)
    },
    closeSideBar: function () {
      this.$emit('clicked')
    },
    profile: function (hashcode, fullname, emailid) {
      this.picture = hashcode
      this.fullname = fullname
      this.emailid = emailid
    },
    logout () {
      window.localStorage.removeItem('refresh')
      window.localStorage.removeItem('access')
      window.localStorage.setItem('username', '')
      this.$data.logged_in = false
      this.$data.username = ''
      window.location.reload()
    }
  }
}
</script>
