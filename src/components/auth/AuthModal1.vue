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
                  <div class="forgot-password"><p @click="openForgotPassword">Forgot Password ?</p></div>
                </div>
              </div>
              <div class="col image-col"></div>
              <div class="col fields-col">
                <div class="fields-inner">
                  <div class="logo"><i class="fas fa-file-alt"></i></div>
                  <!-- Auth First Step -->
                  <div id="auth-first-step" :class="first_step_status">
                    <div class="short-description"><p>Access our features</p></div>
                    <div class="long-description"><p>Please enter the Username you used to sign up on our Website to access all the features including templates, services and support. Note that username is of atleast 4 characters and is unique.</p></div>
                    <div class="auth-input-field" :class="username_field_class">
                      <input type="text" v-model="username" @input="refreshUsernameError" @focus="refreshUsernameError" :class="username_class" spellcheck="false" placeholder="Username" />
                      <div class="field-status"><div v-if="auth_username_valid"><i class="fas fa-check"></i></div><div v-else><i class="fas fa-times"></i></div></div>
                    </div>
                    <div class="first-step-next">
                      <div class="input-email-submit">
                        <div class="continue-loading" v-if="username_loading"><Loading /></div>
                        <p v-else class="submit-email" @click="processUsername">Next <i class="fas fa-chevron-right"></i></p>
                      </div>
                      <div class="form-error" v-if="username_error"><p v-text="username_error"></p></div>
                      <div class="start-signup" v-if="username == '' && username_error == ''"><p @click="createAccount">Create Account</p></div>
                    </div>
                  </div>
                  <!-- End Auth First Step -->
                  <!-- Auth Password Step -->
                  <div id="auth-password-step" :class="password_step_status">
                    <div class="short-description"><p>Enter Password</p></div>
                    <div class="long-description"><p>Enter the password that you used while registered your account with Username <span>{{ username }}</span>. Password is atleast 8 characters long and may contain Numbers, characters & special characters.</p></div>
                    <div class="auth-input-field" :class="password_field_class">
                      <input type="password" v-model="password" @input="refreshPasswordError" @focus="refreshPasswordError" :class="password_class" spellcheck="false" placeholder="Password" />
                      <div class="field-status"><div v-if="auth_password_valid"><i class="fas fa-check"></i></div><div v-else><i class="fas fa-times"></i></div></div>
                    </div>
                    <div class="first-step-next">
                      <div class="input-email-submit">
                        <div class="continue-loading" v-if="password_loading"><Loading /></div>
                        <p v-else class="submit-email" @click="processPassword">Next <i class="fas fa-chevron-right"></i></p>
                      </div>
                      <div class="form-error" v-if="password_error != ''"><p v-text="password_error"></p></div>
                      <div class="cancel-login" v-if="password == '' && password_error == ''"><p class="cancel-password" @click="cancelLogin"><i class="fas fa-chevron-left"></i> Back</p></div>
                    </div>
                  </div>
                  <!-- End Auth Password Step -->
                  <!-- Create Account Step -->
                  <div id="create-account-step" :class="create_account_status">
                    <div class="auth-input-field" :class="fullname_field_class">
                      <input type="text" v-model="fullname" @input="refreshFullname" @focus="refreshFullname" :class="fullname_class" placeholder="Full name" />
                      <div class="field-status"><div v-if="auth_fullname_valid"><i class="fas fa-check"></i></div><div v-else><i class="fas fa-times"></i></div></div>
                    </div>
                    <div class="auth-input-field" :class="register_username_field_class">
                      <input type="text" v-model="register_username" @input="refreshRegisterUsername" @focus="refreshRegisterUsername" :class="register_username_class" placeholder="Username" spellcheck="false" />
                      <div class="field-status"><div v-if="auth_register_username_valid"><i class="fas fa-check"></i></div><div v-else><i class="fas fa-times"></i></div></div>
                    </div>
                    <div class="auth-input-field" :class="email_field_class">
                      <input type="email" v-model="email" @input="refreshEmail" @focus="refreshEmail" :class="email_class" placeholder="email@name.com" spellcheck="false" />
                      <div class="field-status"><div v-if="auth_email_valid"><i class="fas fa-check"></i></div><div v-else><i class="fas fa-times"></i></div></div>
                    </div>
                    <div class="auth-input-field" :class="register_password_field_class">
                      <input type="password" v-model="register_password" @input="refreshRegisterPassword" @focus="refreshRegisterPassword" :class="register_password_class" placeholder="Password" />
                      <div class="field-status"><div v-if="auth_register_password_valid"><i class="fas fa-check"></i></div><div v-else><i class="fas fa-times"></i></div></div>
                    </div>
                    <div class="auth-input-field" :class="confirm_password_field_class">
                      <input type="password" v-model="confirm_password" @input="refreshConfirmPassword" @focus="refreshConfirmPassword" :class="confirm_password_class" placeholder="Confirm password" />
                      <div class="field-status"><div v-if="auth_confirm_password_valid"><i class="fas fa-check"></i></div><div v-else><i class="fas fa-times"></i></div></div>
                    </div>
                    <div class="accept-terms">
                      <input type="checkbox" id="accept-terms" @change="refreshTerms" v-model="accept_terms" />
                      <label for="accept-terms"></label>
                      <p>I agree to the terms of service</p>
                    </div>
                    <div class="register-submit">
                      <div class="input-email-submit">
                        <div class="continue-loading" v-if="register_loading"><Loading /></div>
                        <p v-else class="submit-email" @click="processCreateAccount">Next <i class="fas fa-chevron-right"></i></p>
                      </div>
                      <div class="cancel-register"><p class="cancel-passwor" @click="cancelRegister"><i class="fas fa-chevron-left"></i> Back</p></div>
                    </div>
                    <p class="register-error" v-text="register_error"></p>
                  </div>
                  <!-- End Create Account Step -->
                  <!-- Enter OTP Step -->
                  <div id="otp-step" :class="otp_step_status">
                    <div class="otp-step-inner">
                      <div class="otp-title"><p>Check your Inbox</p></div>
                      <div class="inbox-icon"><i class="fas fa-shipping-fast"></i></div>
                      <div class="otp-instructions"><p>We have sent an Email containing OTP to the Email ID you just submitted. Please enter the OTP to continue.</p></div>
                      <div class="otp-field"><input type="text" @click="refreshOTP" @focus="refreshOTP" v-model="otp" placeholder="XXXXXX" @keypress="onlyNumber" maxlength="6" /></div>
                      <div class="otp-submit-button">
                        <div class="continue-loading" id="otp-loading" v-if="otp_loading"><Loading /></div>
                        <p v-else @click="submitOtp">Submit OTP</p>
                      </div>
                      <div class="otp-submit-error">
                        <p v-text="otp_error"></p>
                      </div>
                    </div>
                  </div>
                  <!-- End Enter OTP Step -->
                  <!-- Signing In Step -->
                  <div id="signing-in-step" :class="signing_in_step_status">
                    <div id="tick-mark">
                      <i class="fas fa-check-circle"></i>
                    </div>
                    <p class="complete-message">Registration complete</p>
                    <p class="logging-in">Logging in </p>
                    <span id="loading-span"></span>
                  </div>
                  <!-- End Signing In Step -->
                </div>
              </div>
              <!-- Forgot Password Step -->
              <div id="forgot-password" :class="forgot_class">
                <div id="forgot-password-vertical">
                  <div id="forgot-password-container">
                    <div id="forgot-password-box">
                      <div @click="closeForgotPassword" id="close-forgot-password">
                        <i class="fas fa-times"></i>
                      </div>
                      <div id="forgot-password-title">
                        <p>Forgot Password</p>
                      </div>
                      <!-- Enter Email ID or Username step -->
                      <div id="enter-email-step" :class="email_forgot_step">
                        <div class="forgot-password-hint">
                          <p>Please enter the Username or Email ID you used to Sign up your Account on Mark My CV. You will receive an OTP on your Email ID to change your Password.</p>
                        </div>
                        <div :class="forgot_field_class">
                          <input type="text" v-model="forgot_field" placeholder="Enter Email ID or Username" @input="refreshForgotPassword" @click="refreshForgotPassword">
                          <div class="submit-button">
                            <div v-if="forgot_loading">
                              <Loading />
                            </div>
                            <div v-else>
                              <i @click="forgotPassword" class="fas fa-paper-plane"></i>
                            </div>
                          </div>
                        </div>
                        <div class="forgot-error">
                          <p>{{ forgot_error }}</p>
                        </div>
                      </div>
                      <!-- End Enter Email ID or Username step -->
                      <!-- Enter OTP step -->
                      <div id="enter-otp-step" :class="otp_forgot_step">
                        <div class="forgot-password-hint">
                          <p>{{ forgot_message }}</p>
                        </div>
                        <div :class="forgot_field_class">
                          <input type="text" v-model="forgot_otp" placeholder="Enter OTP" @input="refreshForgotOtp" @click="refreshForgotOtp">
                          <div class="submit-button">
                            <div v-if="forgot_otp_loading">
                              <Loading />
                            </div>
                            <div v-else>
                              <i @click="submitForgotOtp" class="fas fa-paper-plane"></i>
                            </div>
                          </div>
                        </div>
                        <div v-if="forgot_otp == ''" class="enter-otp-options">
                          <div class="left">
                            <p class="cancel-otp" @click="cancelForgotOtp"><i class="fas fa-chevron-left"></i> Cancel</p>
                          </div>
                          <div class="right">
                            <p class="resend-otp">Resend <i class="fas fa-redo-alt"></i></p>
                          </div>
                        </div>
                        <div class="forgot-error">
                          <p>{{ forgot_otp_error }}</p>
                        </div>
                      </div>
                      <!-- End Enter OTP step -->
                      <!-- New Password step -->
                      <div id="new-password-step" :class="new_password_step">
                        <!--<div class="forgot-password-hint">
                          <p>Please enter the new password that you want to set for your account</p>
                        </div>-->
                        <div :class="forgot_field_class">
                          <input type="password" v-model="new_password" placeholder="Enter new Password" @input="refreshForgotOtp" @click="refreshForgotOtp">
                          <input type="password" v-model="confirm_new_password" placeholder="Confirm new Password" @input="refreshForgotOtp" @click="refreshForgotOtp">
                          <div class="submit-button">
                            <div v-if="new_password_loading">
                              <Loading />
                            </div>
                            <div v-else>
                              <i @click="submitNewPassword" class="fas fa-paper-plane"></i>
                            </div>
                          </div>
                        </div>
                        <div class="forgot-error">
                          <p>{{ forgot_new_password_error }}</p>
                        </div>
                      </div>
                      <!-- End New Password step -->
                    </div>
                  </div>
                </div>
              </div>
              <!-- End Forgot Password Step -->
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
      .modal-box{position: absolute;top: 0;left: 0;width: 100%;height: 100%;padding: 0;border-radius: 5px;overflow: hidden;box-shadow: 0 8px 17px 2px rgba(0,0,0,0.14), 0 3px 14px 2px rgba(0,0,0,0.12), 0 5px 5px -3px rgba(0,0,0,0.2);
        #forgot-password{position: absolute;top: 0;left: 0;width: 100%;height: 100%;z-index: 30;background-color: rgba(0,0,0,0.5);display: table;transition: 250ms;opacity: 0;
          #forgot-password-vertical{display: table-cell;vertical-align: middle;
            #forgot-password-container{width: 40%;margin: 0 auto;overflow: hidden;
              #forgot-password-box{padding: 15px 20px;box-sizing: border-box;background-color: #fff;border-radius: 5px;position: relative;transition: 250ms;
                #close-forgot-password{position: absolute;top: 6px;right: 12px;
                  i{font-size: 14px;cursor: pointer;}
                }
                #forgot-password-title{margin-bottom: 10px;
                  p{font-size: 22px;}
                }
                .forgot-password-hint{margin-bottom: 10px;
                  p{font-size: 10px;font-weight: 500;color: #808e9b;}
                }
                .forgot-error{width: 84%;margin: 0 auto 3px auto;
                  p{font-size: 11px;font-weight: 600;color: #E74C3C;min-height: 17px;}
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
                input{width: 100%;height: 32px;background-color: #eee;padding: 0 10px;box-sizing: border-box;border-radius: 4px;font-size: 12px;text-align: center;font-weight: 600;background-color: #fff;border: 1.5px solid #3d3d3d;
                  &.error{border: 1.5px solid #E74C3C;color: #E74C3C}
                  &.filled + .field-status{transform: translateX(20px);}
                  &[readonly]{background: #2ECC71;color: #fff;}
                }
                .submit-button{float: left;cursor: pointer;}
              }
            }
          }
          &.opened{display: table;opacity: 1;
            #forgot-password-box{transform: scale(1);}
          }
          &.closing{display: table;opacity: 0;
            #forgot-password-box{transform: scale(0.8);}
          }
          &.closed{display: none;opacity: 0;
            #forgot-password-box{transform: scale(0.8);}
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
          .register-submit{
            .input-email-submit{float: right;padding-right: 0;margin-top: 0;}
            .cancel-register{float: left;
              p{color: #f6f6f6;background-color: #E74C3C;display: inline;font-size: 11px;font-weight: 600;border-radius: 4px;padding: 5px 10px;cursor: pointer;transition: 150ms;
                i{margin-right: 2px;transition: 150ms;}
              }
            }
            &:after{clear: both;display: block;content: "";}
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
          .register-error{font-size: 11px;font-weight: 600;color: #e74c3c;margin-top: 5px;margin-left: 4px;}
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
          .accept-terms{padding: 0 3px;margin-top: 5px;
            input{display: none;
              & + label{width: 12px;height: 12px;background-color: #ddd;display: inline-block;margin-right: 5px;border-radius: 2px;vertical-align: middle;background-size: 7px;background-repeat: no-repeat;background-position: center;cursor: pointer;
              }
              &:checked + label{background-image: url('../../images/icons/check.svg');background-size: 8px;}
            }
            p{font-size: 10px;display: inline-block;font-weight: 600;}
          }
          .cancel-login{margin-top: 10px;float: left;
            p{color: #f6f6f6;background-color: #E74C3C;display: inline;font-size: 11px;font-weight: 600;border-radius: 4px;padding: 5px 10px;cursor: pointer;transition: 150ms;
              i{margin-right: 2px;transition: 150ms;}
            }
          }
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
          .continue-loading{background-color: #3d3d3d;width: 56.67px;height: 26px;float: right;border-radius: 4px;margin-top: 1px;}
          .input-email-submit, .register-submit{text-align: right;padding-right: 20%;margin-top: 10px;
            p{color: #eee;background-color: #3d3d3d;display: inline;font-size: 11px;font-weight: 600;border-radius: 4px;padding: 5px 10px;cursor: pointer;transition: 150ms;
              i{margin-left: 2px;}
              &:hover{background-color: lighten(#3d3d3d, 8%);}
            }
          }
          .form-error{font-size: 11px;font-weight: 600;color: #E74C3C;}
          .register-submit{margin-top: 16px;}
          #auth-first-step, #create-account-step, #auth-second-step, #otp-step, #auth-password-step, #signing-in-step{transition: 500ms;
            span{color: #16A085;}
            &.hidden{display: none;}
            &.hiding{display: block;opacity: 0;}
            &.show{display: block;opacity: 1;}
          }
          #create-account-step{margin-top: 6px;
            .auth-input-field{margin-top: 6px;
                &:first-child{margin-top: 20px;}
            }
          }
          #auth-second-step{
            .auth-input-field{margin-top: 12px;}
          }
          #otp-step{
            .otp-title{padding-top: 10px;
              p{font-size: 15px;font-weight: 500;text-align: center;}
            }
            .otp-instructions{margin-top: 8px;
              p{font-size: 11px;font-weight: 600;text-align: center;}
            }
            .otp-field{margin-top: 12px;
              input{width: 83px;height: 26px;margin: 0 auto;display: block;padding: 0 10px;box-sizing: border-box;font-size: 13px;font-weight: bold;border-radius: 4px;text-align: center;border: 1.5px solid #3d3d3d;}
            }
            .inbox-icon{text-align: center;margin-top: 12px;
              i{font-size: 30px;}
            }
            .otp-submit-button{text-align: center;margin-top: 10px;
              .continue-loading{width: 83px;float: none;display: inline-block;
                &:after{clear: both;display: block;content: "";}
              }
              p{color: #eee;background-color: #3d3d3d;display: inline;font-size: 11px;font-weight: 600;border-radius: 4px;padding: 5px 10px;cursor: pointer;transition: 150ms;}
            }
            .otp-submit-error{margin-top: 7px;
              p{font-size: 10px;text-align: center;color: #E74C3C;font-weight: 600;}
            }
          }
        }
        .intro-col, .image-col, .fields-col{position: absolute;top: 0;height: 100%;}
        .close-modal{top: 0;right: 0;border-radius: 0 0 0 5px;
          i{vertical-align: middle;padding: 9px 12px;color: #333;font-size: 13px;color: #f6f6f6;background: #E74C3C;border-radius: 0 5px 0 5px;text-shadow: -1px 1px 2px rgba(0,0,0,0.25);transition: 150ms;
            &:hover{background: #C0392B;}
          }
        }
      }
      #enter-email-step, #enter-otp-step, #new-password-step, #new-password-step{transition: 250ms;
        &.right-hidden{transform: translateX(calc(100% + 20px));display: none;}
        &.right-shown{transform: translateX(calc(100% + 20px));display: block;}
        &.center{transform: translateX(0%);display: block;}
        &.left-shown{transform: translateX(calc(-100% - 20px));display: block;}
        &.left-hidden{transform: translateX(calc(-100% - 20px));display: none;}
      }
      #enter-otp-step{
        .enter-otp-options{width: calc(80% + 20px);margin: 2px auto 0px auto;
          &:after{clear: both;content: "";}
        }
        p{font-weight: 600;cursor: pointer;}
        .left{float: left;
          .cancel-otp{font-size: 11px;color: #E74C3C;padding: 3px 2px;border-radius: 4px;
            i{margin-right: 2px;}
          }
        }
        .right{float: right;
          .resend-otp{font-size: 11px;color: #3498DB;padding: 3px 2px;border-radius: 4px;
            i{font-size: 0.85em;margin-left: 2px;}
          }
        }
      }
      #new-password-step{
        .input-field{margin: 4px auto 4px auto;}
        .input-field input{border: 1.5px solid #3d3d3d !important;border-radius: 4px !important;margin-bottom: 6px;width: 100% !important;text-align: center !important;}
        .forgot-error{margin-bottom: 1px;}
        .submit-button{width: 100% !important;border-radius: 4px !important;}
      }
      #signing-in-step{
        #tick-mark{text-align: center;padding-top: 10px;
          i{font-size: 78px;color: #2ECC71;}
        }
        p.complete-message{font-size: 12px;text-align: center;margin-top: 10px;font-weight: 600;}
        p.logging-in{font-size: 12px;text-align: center;margin-top: 58px;font-weight: 600;}
        #loading-span{display: block;width: 80%;margin: 8px auto 0 auto;height: 10px;border-radius: 5px;overflow: hidden;background-color: #eee;
          &:after{display: block;content: "";height: 100%;background-color: #2ECC71;animation-name: pulse;animation-duration: 2s;animation-iteration-count: infinite;}
        }
      }
    }
  }
  @-webkit-keyframes pulse {
    0% { width: 0% }
    100% { width: 100% }
  }
}
@media (max-width: 730px) {
  #auth-modal{
    .modal-vertical{
      .modal-container{width: calc(100% - 30px);
        .modal-box{width: 100%;
          .col.intro-col{width: 0%;overflow: hidden}
          .col.image-col{width: 35%;left: 0;top: 0;}
          .col.fields-col{width: 65%;left: 35%;top: 0;padding: 25px 18px;
            .long-description{width: 90%;}
            .auth-input-field input{width: 80%;}
          }
        }
      }
    }
  }
}
</style>

<script>
import axios from 'axios'
import Loading from '@/components/common/Loading'
export default {
  name: 'AuthModal',
  props: { status: String },
  computed: {
    computedStatus: function () { return 'modal ' + this.$props.status }
  },
  data () {
    return {
      first_step_status: '', username: '', username_field_class: '', username_class: '', auth_username_valid: '', username_error: '', username_loading: '', password_step_status: 'hidden', password: '', password_field_class: '', password_class: '', auth_password_valid: '', password_error: '', password_loading: '', create_account_status: 'hidden', fullname_field_class: '', fullname: '', fullname_class: '', auth_fullname_valid: '', register_username_field_class: '', register_username: '', register_username_class: '', auth_register_username_valid: '', email: '', email_field_class: '', email_class: '', auth_email_valid: '', register_password_field_class: '', register_password: '', register_password_class: '', auth_register_password_valid: '', confirm_password_field_class: '', confirm_password: '', confirm_password_class: '', auth_confirm_password_valid: '', register_loading: false, accept_terms: false, accept_terms_class: '', otp_step_status: 'hidden', otp_error: '', register_error: '', otp: '', otp_loading: false, forgot_loading: false, forgot_class: 'closed', forgot_field: '', forgot_error: '', forgot_field_class: 'input-field', otp_forgot_step: 'right-hidden', email_forgot_step: 'center', forgot_otp: '', forgot_otp_loading: false, forgot_otp_error: '', new_password_step: 'right-hidden', new_password_loading: false, new_password: '', confirm_new_password: '', forgot_message: '', forgot_new_password_error: '', signing_in_step_status: 'hidden'
    }
  },
  components: {
    Loading
  },
  methods: {
    closeModal () {
      this.$emit('closeAuthModal')
      let data = this.$data
      setTimeout(function () {
        data.first_step_status = ''
        data.username = ''
        data.username_field_class = ''
        data.username_class = ''
        data.auth_username_valid = ''
        data.username_error = ''
        data.username_loading = ''
        data.password_step_status = 'hidden'
        data.password = ''
        data.password_field_class = ''
        data.password_class = ''
        data.auth_password_valid = ''
        data.password_error = ''
        data.password_loading = ''
        data.create_account_status = 'hidden'
        data.fullname_field_class = ''
        data.fullname = ''
        data.fullname_class = ''
        data.auth_fullname_valid = ''
        data.register_username_field_class = ''
        data.register_username = ''
        data.register_username_class = ''
        data.auth_register_username_valid = ''
        data.email = ''
        data.email_field_class = ''
        data.email_class = ''
        data.auth_email_valid = ''
        data.register_password_field_class = ''
        data.register_password = ''
        data.register_password_class = ''
        data.auth_register_password_valid = ''
        data.confirm_password_field_class = ''
        data.confirm_password = ''
        data.confirm_password_class = ''
        data.auth_confirm_password_valid = ''
        data.register_loading = false
        data.accept_terms = false
        data.accept_terms_class = ''
        data.otp_step_status = 'hidden'
        data.otp_error = ''
        data.register_error = ''
        data.otp = ''
      }, 500)
    },
    // Username Field Code
    refreshUsernameError () {
      let data = this.$data
      if (data.username === '') {
        setTimeout(function () { data.auth_username_valid = false }, 250)
      } else if ((data.username.length > 0 && data.username.length <= 3) || !/^[a-zA-Z0-9]+$/.test(data.username)) {
        data.auth_username_valid = false
      } else {
        data.auth_username_valid = true
      }
      data.username_error = ''
      data.username_class = (data.username === '') ? '' : 'filled'
    },
    processUsername () {
      let data = this.$data
      if (data.username === '') {
        data.username_class = 'error'
        data.username_field_class = 'shaking'
        setTimeout(function () { data.username_field_class = '' }, 650)
      } else if ((data.username.length > 0 && data.username.length <= 3) || !/^[a-zA-Z0-9]+$/.test(data.username)) {
        data.username_class = 'filled error'
        data.auth_username_valid = false
        data.username_field_class = 'shaking'
        data.username_error = 'Invalid Username'
        setTimeout(function () { data.username_field_class = '' }, 650)
      } else {
        data.username_loading = true
        axios.post('http://localhost:8000/auth/user-exists', { 'username': data.username }).then(function (response) {
          if (response.data.exists === false) {
            data.username_class = 'filled error'
            data.auth_username_valid = false
            data.username_field_class = 'shaking'
            data.username_error = 'Incorrect Username'
            data.username_loading = false
            setTimeout(function () { data.username_field_class = '' }, 650)
          } else {
            data.first_step_status = 'hiding'
            setTimeout(function () {
              data.first_step_status = 'hidden'
              data.password_step_status = 'hiding'
              setTimeout(function () {
                data.password_step_status = 'show'
              }, 250)
            }, 250)
          }
        }).catch(function (error) {
          console.log(error)
        }).finally(function () { })
      }
    },
    // End Username Field Code
    // Password Field Code
    refreshPasswordError () {
      let data = this.$data
      if (data.password === '') {
        setTimeout(function () {
          data.auth_password_valid = false
        }, 250)
      } else if (data.password.length > 0 && data.password.length < 8) {
        data.auth_password_valid = false
      } else {
        data.auth_password_valid = true
      }
      data.password_error = ''
      data.password_class = (data.password === '') ? '' : 'filled'
    },
    processPassword () {
      let target = this
      let data = this.$data
      if (data.password === '') {
        data.password_class = 'error'
        data.password_field_class = 'shaking'
        setTimeout(function () { data.password_field_class = '' }, 650)
      } else if (data.password.length > 0 && data.password.length <= 8) {
        data.password_class = 'filled error'
        data.auth_password_valid = false
        data.password_field_class = 'shaking'
        data.password_error = 'Invalid Password'
        setTimeout(function () { data.password_field_class = '' }, 650)
      } else {
        data.password_loading = true
        axios.post('http://localhost:8000/api/token/', {
          'username': data.username,
          'password': data.password
        }).then(function (response) {
          if (response.status === 200) {
            data.password_step_status = 'hiding'
            setTimeout(function () {
              data.passwordStepStatus = 'hidden'
              window.localStorage.setItem('refresh', response.data.refresh)
              window.localStorage.setItem('access', response.data.access)
              window.localStorage.setItem('username', data.username)
              target.$emit('closeAuthModal')
              window.location.reload()
            }, 250)
          }
        }).catch(function (error) {
          if (error.response.status === 401) {
            data.password_class = 'filled error'
            data.auth_password_valid = false
            data.password_field_class = 'shaking'
            data.password_error = 'Wrong Password'
            data.password_loading = false
            setTimeout(function () { data.password_field_class = '' }, 650)
          } else {
            data.password_error = 'Unknown Error'
            data.password_loading = false
          }
        }).finally(function () { })
      }
    },
    cancelLogin () {
      let data = this.$data
      data.password_step_status = 'hiding'
      data.username_loading = false
      setTimeout(function () {
        data.password_step_status = 'hidden'
        data.first_step_status = 'hiding'
        setTimeout(function () {
          data.first_step_status = 'show'
        }, 250)
      }, 250)
    },
    // End Password Field Code
    createAccount () {
      let data = this.$data
      data.first_step_status = 'hiding'
      setTimeout(function () {
        data.first_step_status = 'hidden'
        data.create_account_status = 'hiding'
        setTimeout(function () {
          data.create_account_status = 'show'
        }, 250)
      }, 250)
    },
    // Create Account Fields Code
    refreshFullname () {
      let data = this.$data
      if (data.fullname === '') {
        setTimeout(function () { data.auth_fullname_valid = false }, 250)
      } else if (data.fullname.length > 0 && data.fullname.length <= 3) {
        data.auth_fullname_valid = false
      } else {
        data.auth_fullname_valid = true
      }
      data.fullname_class = (data.fullname === '') ? '' : 'filled'
    },
    refreshRegisterUsername () {
      let data = this.$data
      data.register_error = ''
      if (data.register_username === '') {
        setTimeout(function () { data.auth_register_username_valid = false }, 250)
      } else if ((data.register_username.length > 0 && data.register_username.length <= 3) || !/^[a-zA-Z0-9]+$/.test(data.register_username)) {
        data.auth_register_username_valid = false
      } else {
        data.auth_register_username_valid = true
      }
      data.register_username_class = (data.register_username === '') ? '' : 'filled'
    },
    refreshEmail () {
      let data = this.$data
      data.register_error = ''
      if (data.email === '') {
        setTimeout(function () { data.auth_email_valid = false }, 250)
      } else if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(data.email)) {
        data.auth_email_valid = false
      } else {
        data.auth_email_valid = true
      }
      data.email_class = (data.email === '') ? '' : 'filled'
    },
    refreshRegisterPassword () {
      let data = this.$data
      if (data.register_password === '') {
        setTimeout(function () { data.auth_register_password_valid = false }, 250)
      } else if (data.register_password.length > 0 && data.register_password.length <= 7) {
        data.auth_register_password_valid = false
      } else {
        data.auth_register_password_valid = true
      }
      data.register_password_class = (data.register_password === '') ? '' : 'filled'
    },
    refreshConfirmPassword () {
      let data = this.$data
      if (data.confirm_password === '') {
        setTimeout(function () { data.auth_confirm_password_valid = false }, 250)
      } else if ((data.confirm_password.length > 0 && data.confirm_password.length <= 7) || data.confirm_password !== data.register_password) {
        data.auth_confirm_password_valid = false
      } else {
        data.auth_confirm_password_valid = true
      }
      data.confirm_password_class = (data.confirm_password === '') ? '' : 'filled'
    },
    refreshTerms () {
      let data = this.$data
      data.register_error = ''
    },
    processCreateAccount () {
      let data = this.$data
      data.register_error = ''
      if (!data.auth_fullname_valid) {
        data.fullname_class = 'filled error'
        data.auth_fullname_valid = false
        data.fullname_field_class = 'shaking'
        setTimeout(function () { data.fullname_field_class = '' }, 650)
      }
      if (!data.auth_register_username_valid) {
        data.register_username_class = 'filled error'
        data.auth_register_username_valid = false
        data.register_username_field_class = 'shaking'
        setTimeout(function () { data.register_username_field_class = '' }, 650)
      }
      if (!data.auth_email_valid) {
        data.email_class = 'filled error'
        data.auth_register_email_valid = false
        data.email_field_class = 'shaking'
        setTimeout(function () { data.email_field_class = '' }, 650)
      }
      if (!data.auth_register_password_valid) {
        data.register_password_class = 'filled error'
        data.auth_register_password_valid = false
        data.register_password_field_class = 'shaking'
        setTimeout(function () { data.register_password_field_class = '' }, 650)
      }
      if (!data.auth_confirm_password_valid) {
        data.confirm_password_class = 'filled error'
        data.auth_confirm_password_valid = false
        data.confirm_password_field_class = 'shaking'
        setTimeout(function () { data.confirm_password_field_class = '' }, 650)
      }
      if (!data.accept_terms) {
        data.register_error = 'Please agree to Terms to continue'
      }
      if (data.auth_fullname_valid && data.auth_register_username_valid && data.auth_email_valid && data.auth_register_password_valid && data.auth_confirm_password_valid && data.accept_terms) {
        data.register_loading = true
        axios.post('http://localhost:8000/auth/create-account', {
          'fullname': data.fullname,
          'username': data.register_username,
          'emailid': data.email,
          'password': data.register_password
        }).then(function (response) {
          if (response.status === 200) {
            if (response.data.status === 'ok') {
              axios.post('http://localhost:8000/api/token/', {
                'username': data.register_username,
                'password': data.register_password
              }).then(function (response) {
                if (response.status === 200) {
                  setTimeout(function () {
                    window.localStorage.setItem('refresh', response.data.refresh)
                    window.localStorage.setItem('access', response.data.access)
                    window.localStorage.setItem('username', data.register_username)
                    data.create_account_status = 'hiding'
                    setTimeout(function () {
                      data.create_account_status = 'hidden'
                      data.otp_step_status = 'hiding'
                      setTimeout(function () {
                        data.otp_step_status = 'show'
                      }, 250)
                    }, 250)
                  }, 250)
                }
              }).catch(function (error) {
                console.log(error)
              }).finally(function () { })
            } else if (response.data.status === 'error') {
              data.register_error = response.data.message
              data.register_loading = false
            }
          }
        }).catch(function (error) {
          if (error.response.status === 401) {
            data.password_class = 'filled error'
            data.auth_password_valid = false
            data.password_field_class = 'shaking'
            data.password_error = 'Wrong Password'
            data.password_loading = false
            setTimeout(function () { data.password_field_class = '' }, 650)
          }
        }).finally(function () { })
      }
    },
    cancelRegister () {
      let data = this.$data
      let target = this
      data.create_account_status = 'hiding'
      data.register_loading = false
      setTimeout(function () {
        data.create_account_status = 'hidden'
        data.first_step_status = 'hiding'
        data.fullname = ''
        data.register_username = ''
        data.email = ''
        data.register_password = ''
        data.confirm_password = ''
        data.accept_terms = false
        target.refreshFullname()
        target.refreshRegisterUsername()
        target.refreshEmail()
        target.refreshRegisterPassword()
        target.refreshConfirmPassword()
        setTimeout(function () {
          data.first_step_status = 'show'
        }, 250)
      }, 250)
    },
    // End Create Account Fields Code
    // Forgot Password Code
    forgotPassword () {
      let data = this.$data
      if (data.forgot_field === '') {
        data.forgot_error = 'Field cannot be empty'
        data.forgot_field_class = 'input-field shaking error'
        setTimeout(function () {
          data.forgot_field_class = 'input-field error'
        }, 650)
      } else if (!/^[a-zA-Z0-9]+$/.test(data.forgot_field) && !/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(data.forgot_field)) {
        data.forgot_error = 'Invalid Username of Email ID'
        data.forgot_field_class = 'input-field shaking error'
        setTimeout(function () {
          data.forgot_field_class = 'input-field error'
        }, 650)
      } else {
        data.forgot_loading = true
        axios.post('http://localhost:8000/auth/reset-password', {
          'value': data.forgot_field
        }).then(function (response) {
          if (response.data.status === 'success') {
            data.forgot_message = response.data.message
            data.otp_forgot_step = 'right-hidden'
            data.email_forgot_step = 'left-shown'
            setTimeout(function () {
              data.otp_forgot_step = 'right-shown'
              data.email_forgot_step = 'left-hidden'
              setTimeout(function () {
                data.otp_forgot_step = 'center'
                data.email_forgot_step = 'left-hidden'
              }, 10)
            }, 250)
          } else if (response.data.status === 'error') {
            data.forgot_error = response.data.message
            data.forgot_loading = false
            data.forgot_field_class = 'input-field shaking error'
            setTimeout(function () {
              data.forgot_field_class = 'input-field error'
            }, 650)
          }
        }).catch(function (error) {
          console.log(error)
        }).finally(function () { })
      }
    },
    openForgotPassword () {
      let data = this.$data
      data.forgot_class = 'closing'
      setTimeout(function () {
        data.forgot_class = 'opened'
      }, 10)
    },
    closeForgotPassword () {
      let data = this.$data
      data.forgot_class = 'closing'
      setTimeout(function () {
        data.forgot_class = 'closed'
        data.forgot_loading = false
        data.forgot_class = 'closed'
        data.forgot_field = ''
        data.forgot_error = ''
        data.forgot_field_class = 'input-field'
        data.otp_forgot_step = 'right-hidden'
        data.email_forgot_step = 'center'
        data.forgot_otp = ''
        data.forgot_otp_loading = false
        data.forgot_otp_error = ''
        data.new_password_step = 'right-hidden'
        data.new_password_loading = false
        data.new_password = ''
        data.confirm_new_password = ''
      }, 250)
    },
    refreshForgotPassword () {
      let data = this.$data
      data.forgot_error = ''
      data.forgot_field_class = 'input-field'
    },
    // End Forgot Password Code
    submitOtp () {
      let data = this.$data
      let emitter = this
      let access = window.localStorage.getItem('access')
      console.log('Bearer ' + access)
      if (data.otp.length === 6) {
        data.otp_loading = true
        axios({
          method: 'post',
          url: 'http://localhost:8000/auth/submit-otp',
          data: {
            'otp': data.otp
          },
          headers: {
            Authorization: 'Bearer ' + access
          }
        }).then(function (response) {
          if (response.data.status === 'ok') {
            emitter.$emit('setUsername', data.register_username)
            emitter.$emit('closeAuthModal')
            setTimeout(function () {
              window.location.reload()
            }, 500)
          } else if (response.data.status === 'error') {
            data.otp_error = response.data.message
            data.otp_loading = false
          }
        }).catch(function (error) {
          console.log(error)
        }).finally(function () { })
      } else {
        data.otp_error = 'Enter 6 digit OTP'
      }
    },
    onlyNumber ($event) {
      let keyCode = ($event.keyCode ? $event.keyCode : $event.which)
      if ((keyCode < 48 || keyCode > 57) && keyCode !== 46) {
        $event.preventDefault()
      }
    },
    refreshOTP () {
      let data = this.$data
      data.otp_error = ''
    },
    refreshForgotOtp () {
      let data = this.$data
      data.forgot_otp_error = ''
    },
    submitForgotOtp () {
      let data = this.$data
      data.forgot_otp_loading = true
      axios.post('http://localhost:8000/auth/forgot-otp', {
        'value': data.forgot_field,
        'otp': data.forgot_otp
      }).then(function (response) {
        if (response.data.status === 'success') {
          data.new_password_step = 'right-hidden'
          data.otp_forgot_step = 'left-shown'
          setTimeout(function () {
            data.new_password_step = 'right-shown'
            data.otp_forgot_step = 'left-hidden'
            setTimeout(function () {
              data.new_password_step = 'center'
              data.otp_forgot_step = 'left-hidden'
            }, 10)
          }, 250)
        } else if (response.data.status === 'error') {
          data.forgot_otp_error = response.data.message
          data.forgot_otp_loading = false
        }
      }).catch(function (error) {
        console.log(error)
      }).finally(function () { })
    },
    cancelForgotOtp () {
      let data = this.$data
      data.forgot_loading = false
      data.otp_forgot_step = 'right-shown'
      data.email_forgot_step = 'left-hidden'
      setTimeout(function () {
        data.otp_forgot_step = 'right-hidden'
        data.email_forgot_step = 'left-shown'
        setTimeout(function () {
          data.otp_forgot_step = 'right-hidden'
          data.email_forgot_step = 'center'
        }, 10)
      }, 250)
    },
    submitNewPassword () {
      let data = this.$data
      let emitter = this
      if ((data.new_password === data.confirm_new_password) && data.new_password.length >= 8 && data.confirm_new_password.length >= 8) {
        data.new_password_loading = true
        axios.post('http://localhost:8000/auth/forgot-otp', {
          'value': data.forgot_field,
          'otp': data.forgot_otp
        }).then(function (response) {
          if (response.data.status === 'success') {
            // emitter.$emit('setUsername', data.register_username)
            emitter.closeForgotPassword()
          } else if (response.data.status === 'error') {
            data.forgot_otp_error = response.data.message
            data.forgot_otp_loading = false
          }
        }).catch(function (error) {
          console.log(error)
        }).finally(function () { })
      } else if (data.new_password.length < 8 || data.confirm_new_password.length < 8) {
        data.forgot_new_password_error = 'Atleast 8 Characters'
      } else {
        data.forgot_new_password_error = 'Passwords do not match'
      }
    }
  }
}
</script>
