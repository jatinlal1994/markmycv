<template>
  <div>
    <div id="top-nav">
      <div id="top-nav-left">
        <div id="menu-button" @click="toggleSideBar"><i class="fas fa-bars"></i> Account</div>
      </div>
      <div id="top-nav-center">
        <router-link to="/">
          <p>MarkMyCV</p>
        </router-link>
      </div>
      <div id="top-nav-right">
        <div v-if="logged_in" class="nav-menu-button">
          <p class="username-p"><span v-text="username"></span></p>
          <div id="dropdown">
            <p class="logout-button" @click="logoutPopup">Logout <i class="fas fa-sign-out-alt"></i></p>
            <div id="logout-popup" :class="logout_popup_class">
              <div id="logout-popup-inner">
                <p class="confirm-title">Confirm ?</p>
                <p class="confirm-text">Are you sure you want to logout ?</p>
                <div class="popup-row">
                  <div class="no">
                    <p @click="cancelPopup"><i class="fas fa-times"></i> No</p>
                  </div>
                  <div class="yes">
                    <p @click="logout">Yes<i class="fas fa-check"></i></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div v-else class="nav-button" @click="openAuthModal"><p>Login <i class="fas fa-sign-in-alt"></i></p></div>
      </div>
    </div>
    <SideMenuBar :status="sideBarStatus" :logged="logged_in" :username="username" @clicked="toggleSideBar" />
    <AuthModal @closeAuthModal="closeAuthModal" @setUsername="setUsername" :status="authModalStatus" />
    <div id="logout-popup-overlay" :class="logout_popup_class"></div>
  </div>
</template>

<style lang="scss">
#top-nav{position: fixed;top: 0;left: 0;width: 100%;height: 42px;z-index: 1;padding: 0px 3%;box-sizing: border-box;background-color: #fff;
  &-left{float: left;
    #menu-button{line-height: 42px;font-weight: 600;padding: 0 10px;transition: 150ms;cursor: pointer;font-size: 13px;color: #333;position: relative;
      &, i{vertical-align: middle;}
      i{margin-right: 3px;font-size: 1.2em;}
      &:after{position: absolute;top: 0;left: 0;width: 100%;height: 100%;z-index: -1;background-color: transparent;display: block;content: "";transition: 250ms;border-radius: 4px;transform: translateY(-4px);}
      &:hover{
        &:after{background-color: darken(#1ABC9C, 5%);background-color: rgba(255,255,255,0.1);transform: translateY(0px);}
      }
    }
  }
  &-center{position: fixed;left: calc(50vw - 60px);top: 10px;
    p{font-family: 'Barcelony', sans-serif;font-weight: bold;color: #333;font-size: 14px;}
  }
  &-right{float: right;
    p{font-weight: 600;padding: 0 15px;transition: 150ms;color: #333;font-size: 13px;position: relative;
      i{margin-left: 3px;font-size: 1.2em;}
      &, i{vertical-align: middle;line-height: 42px;}
      &:after{position: absolute;top: 0;left: 0;width: 100%;height: 100%;background-color: transparent;display: block;content: "";z-index: -1;transition: 250ms;border-radius: 4px;transform: translateY(-4px);}
    }
    #dropwown{
      p{
        &:hover{
          &:after{background-color: darken(#1ABC9C, 5%);background-color: rgba(255,255,255,0.1);transform: translateY(0px);}
        }
      }
      .logout-button{
        &:hover{
          &:after{background-color: darken(#1ABC9C, 5%);background-color: rgba(255,255,255,0.1);transform: translateY(0px);}
        }
      }
    }
  }
  &:after{clear: both;display: block;content: "";}
}
.nav-button{cursor: pointer;}
#top-nav-right{
  .nav-menu-button{
    p{float: left;
      span{float: left;}
      i{float: left;margin-left: 8px;}
      &:after{clear: both;display: block;content: "";}
    }
    #dropdown{float: left;border-radius: 5px;font-weight: 500;
      i{float: right}
    }
  }
}
.nav-menu-button{position: relative;
  #dropdown{position: relative;
    p.logout-button{background-color: #E74C3C;text-align: center;transition: 250ms;border-radius: 5px;cursor: pointer;}
    #logout-popup{display: none;opacity: 0;transition: 250ms;transform: translateY(-20px);
      &.opening{display: block;opacity: 0;transform: translate(12px, -10px) scale(0.8);}
      &.open{display: block;opacity: 1;transform: translate(0px, 0px) scale(1);}
    }
    #logout-popup-inner{position: absolute;right: -5px;top: 50px;width: 180px;background-color: #fff;border-radius: 4px;z-index: 5;box-shadow: 0 8px 17px 2px rgba(0,0,0,0.14), 0 3px 14px 2px rgba(0,0,0,0.12), 0 5px 5px -3px rgba(0,0,0,0.2);
      .confirm-title{font-size: 12px;text-align: center;background-color: #e74c3c;width: 100%;box-sizing: border-box;line-height: 28px;color: #fff;border-radius: 4px 4px 0 0;}
      .confirm-text{background-color: #fff;color: #34495E;line-height: 16px;font-weight: 500;font-size: 11px;padding: 6px 12px;margin-bottom: 2px;}
      .popup-row{padding: 0 10px 10px 10px;
        .no{float: left;
          p{background-color: #E74C3C;cursor: pointer;
            i{margin-right: 4px;}
            &:hover{background-color: #C0392B}
          }
        }
        .yes{float: right;
          p{background-color: transparent;background-color: #2ECC71;cursor: pointer;
            i{margin-left: 4px;}
            &:hover{background-color: #27AE60;}
          }
        }
        p{line-height: 22px;font-size: 11px;border-radius: 4px;padding: 0 10px;font-weight: 600;
          i{line-height: 22px;font-size: 11px;float: none;margin: 0;}
        }
        &:after{clear: both;display: block;content: "";}
      }
      &:after{display: block;content: "";position: absolute;top: -6px;right: 54px;width: 12px;height: 12px;background-color: #e74c3c;transform: rotate(45deg);}
    }
  }
}
@media (max-width: 560px) {
  .username-p{display: none;}
}
</style>

<script>
import SideMenuBar from '@/components/common/SideMenuBar'
import AuthModal from '@/components/auth/AuthModal'

export default {
  name: 'Nav',
  components: { SideMenuBar, AuthModal },
  data () {
    return { sideBarStatus: 'closed', authModalStatus: 'closed', logged_in: false, username: '', logout_popup_class: 'closed' }
  },
  created () {
    let data = this.$data
    let userLoggedIn = window.localStorage.getItem('username')
    if (userLoggedIn === '' || userLoggedIn === null) {
      data.logged_in = false
      data.username = ''
      if (this.$router.currentRoute.path !== '/') {
        this.$router.push('/')
      }
    } else {
      data.logged_in = true
      data.username = userLoggedIn
    }
  },
  methods: {
    toggleSideBar () {
      if (this.$data.sideBarStatus === 'closed') {
        this.$data.sideBarStatus = 'opened'
        this.$emit('closeHome', 'opened')
      } else {
        this.$data.sideBarStatus = 'closed'
        this.$emit('closeHome', '')
      }
    },
    openAuthModal () {
      let status = this.$data
      status.authModalStatus = 'opened'
      status.authModalStatus = 'opening'
      setTimeout(function () {
        status.authModalStatus = 'opened'
      }, 10)
    },
    closeAuthModal () {
      let status = this.$data
      status.authModalStatus = 'opening'
      setTimeout(function () {
        status.authModalStatus = 'closed'
      }, 500)
    },
    setUsername (username) {
      this.$data.logged_in = true
      this.$data.username = username
    },
    logoutPopup () {
      let data = this.$data
      data.logout_popup_class = 'opening'
      setTimeout(function () {
        data.logout_popup_class = 'open'
      }, 10)
    },
    logout () {
      window.localStorage.removeItem('refresh')
      window.localStorage.removeItem('access')
      window.localStorage.setItem('username', '')
      this.$data.logged_in = false
      this.$data.username = ''
      window.location.reload()
    },
    cancelPopup () {
      let data = this.$data
      data.logout_popup_class = 'opening'
      setTimeout(function () {
        data.logout_popup_class = 'closed'
      }, 260)
    }
  }
}
</script>
