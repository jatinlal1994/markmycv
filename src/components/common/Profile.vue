<template>
<div>
  <div id="profile-modal" :class="computedStatus">
    <div class="modal-vertical">
      <div class="modal-container">
        <div class="modal-box">
          <!-- <div id="image-cropper">
            <ImageCropper />
          </div> -->
          <div id="skill-editor" :class="skill_editor_class">
            <div class="inner-editor-vertical">
              <div class="inner-editor-inner">
                <div class="sub-modal-title">
                  <p>{{ temp_skill_title }}</p>
                </div>
                <div class="sub-modal-body">
                  <div class="input-field skill-type">
                    <input type="text" v-model="temp_skill_header" placeholder="Skill Type">
                  </div>
                  <div class="textarea-field skill-desc">
                    <textarea v-model="temp_skill_description" placeholder="Skill Description"></textarea>
                  </div>
                </div>
                <div class="sub-modal-buttons">
                  <div class="button cancel">
                    <p @click="cancelSkill"><i class="fas fa-times"></i>Cancel</p>
                  </div>
                  <div class="button save">
                    <p v-if="temp_skill_title == 'Add Skillset'" @click="addSkill">Add<i class="fas fa-save"></i></p>
                    <p v-else-if="temp_skill_title == 'Edit Skillset'" @click="saveEditSkill()">Save<i class="fas fa-save"></i></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div id="career-editor" :class="career_editor_class">
            <div class="inner-editor-vertical">
              <div class="inner-editor-inner">
                <div class="sub-modal-title">
                  <p>{{ temp_career_title }}</p>
                </div>
                <div class="sub-modal-body">
                  <div class="input-field  organisation-name">
                    <label>Organisation name</label>
                    <input type="text" v-model="temp_organisation_name" placeholder="Organisation Name">
                  </div>
                  <div class="input-field  organisation-name">
                    <label>Position</label>
                    <input type="text" v-model="temp_position" placeholder="Position">
                  </div>
                  <div class="fields-row">
                    <div class="input-field col duration">
                      <label>From</label>
                      <input type="text" v-model="temp_duration_start" placeholder="Month, Year">
                    </div>
                    <div class="input-field col duration">
                      <label>To</label>
                      <input type="text" v-model="temp_duration_end" placeholder="Month, Year">
                    </div>
                  </div>
                  <div class="textarea-field achievement" v-for="(achievement, count) in temp_achievements" :key="count">
                    <div class="achievement-row">
                      <label>Achievement {{ (count + 1) }}</label>
                      <div class="achievement-delete">
                        <i class="fas fa-trash"></i>
                      </div>
                    </div>
                    <textarea v-model="achievement.data" placeholder="Job achievements"></textarea>
                  </div>
                  <div>
                    <div id="add-temp-achievement">
                      <div id="add-temp-achievement-inner">
                        <p @click="addAchievement"><i class="fas fa-plus"></i> Add achievement</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="sub-modal-buttons">
                  <div class="button cancel">
                    <p @click="cancelCareer"><i class="fas fa-times"></i>Cancel</p>
                  </div>
                  <div class="button save">
                    <p v-if="temp_career_title == 'Add Career Step'" @click="addCareer">Add<i class="fas fa-save"></i></p>
                    <p v-else-if="temp_career_title == 'Edit Career Step'" @click="saveEditCareer">Save<i class="fas fa-save"></i></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div id="education-editor" :class="education_editor_class">
            <div class="inner-editor-vertical">
              <div class="inner-editor-inner">
                <div class="sub-modal-title">
                  <p>{{ temp_education_title }}</p>
                </div>
                <div class="sub-modal-body">
                  <div class="input-field  organisation-name">
                    <label>Course name</label>
                    <input type="text" v-model="temp_course_name" placeholder="Course Name">
                  </div>
                  <div class="input-field  organisation-name">
                    <label>College/Institute name</label>
                    <input type="text" v-model="temp_institute_name" placeholder="Institute Name">
                  </div>
                  <div class="fields-row">
                    <div class="input-field col duration">
                      <label>From</label>
                      <input type="text" v-model="temp_education_start" placeholder="Month, Year">
                    </div>
                    <div class="input-field col duration">
                      <label>To</label>
                      <input type="text" v-model="temp_education_end" placeholder="Month, Year">
                    </div>
                  </div>
                  <div class="input-field  organisation-name">
                    <label>Marks obtained</label>
                    <input type="text" v-model="temp_education_score" placeholder="In % or C.G.P.A.">
                  </div>
                </div>
                <div class="sub-modal-buttons">
                  <div class="button cancel">
                    <p @click="cancelEducation"><i class="fas fa-times"></i>Cancel</p>
                  </div>
                  <div class="button save">
                    <p v-if="temp_education_title == 'Add Education'" @click="addEducation">Add<i class="fas fa-save"></i></p>
                    <p v-else-if="temp_education_title == 'Edit Education'" @click="saveEditEducation">Save<i class="fas fa-save"></i></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div id="profile-modal-loader" :class="modal_loader">
            <div id="profile-modal-loader-inner">
              <Loading />
            </div>
          </div>
          <div class="close-modal" @click="closeModal"><i class="fas fa-times"></i></div>
          <div class="modal-title"><p>My Profile</p></div>
          <div id="profile-main-content">
            <div id="profile-basic-info">
              <div class="profile-image">
                <img width="185" height="185" alt="Profile Image" :src="profile_picture">
                <input type="file" id="profile-image-upload" @change="onImageChange">
                <label for="profile-image-upload" id="edit-picture">
                  <div id="edit-picture-vertical">
                    <i class="fas fa-camera"></i>
                    <p>Upload</p>
                  </div>
                </label>
              </div>
              <div class="profile-basics">
                <div class="fields">
                  <div class="field"><i class="fas fa-user"></i><input type="text" v-model="fullname" placeholder="Full name" @input="refreshSave" /></div>
                  <div class="field"><i class="fas fa-crosshairs"></i><input type="text" v-model="position" placeholder="Job Position" @input="refreshSave" /></div>
                  <div class="field"><i class="fas fa-map-marker-alt"></i><input type="text" v-model="location" placeholder="Location" @input="refreshSave" /></div>
                  <div class="field"><i class="fas fa-envelope"></i><input type="text" v-model="email_id" placeholder="Email ID" @input="refreshSave" /></div>
                  <div class="field"><i class="fas fa-phone"></i><input type="text" v-model="contact_no" placeholder="Contact No." @input="refreshSave" /></div>
                </div>
              </div>
            </div>
            <div class="profile-modal-title">
              <div class="profile-modal-title-inner"><p>Short Summary</p></div>
            </div>
            <div class="short-summary">
              <textarea v-model="summary" placeholder="A short summary about your career" @input="refreshSave"></textarea>
            </div>
            <div class="profile-modal-title">
              <div class="profile-modal-title-inner"><p>Career Objective</p></div>
            </div>
            <div class="short-summary">
              <textarea v-model="objective" placeholder="Enter your Career Objective" @input="refreshSave"></textarea>
            </div>
            <div class="profile-modal-title">
              <div class="profile-modal-title-inner"><p>Core skills</p></div>
            </div>
            <div class="short-summary">
              <textarea v-model="core_skills" placeholder="Skill Name 1 - Skill Name 2 - Skill Name 3 - Skill Name 4 - Skill Name 5 - Skill Name 6 - Skill Name 7 - Skill Name 8" @input="refreshSave"></textarea>
            </div>
            <div class="profile-modal-title">
              <div class="profile-modal-title-inner"><p>Other Skills</p></div>
              <div class="add-skill-button" @click="openSkillModal"><p><i class="fas fa-plus"></i> Add Skillset</p></div>
            </div>
            <div id="profile-skills">
              <div class="no-skills" v-if="skills.length == 0">
                <p>You have not added any Career step. Click on Add Step button to add a Career Step</p>
              </div>
              <div class="profile-skill" v-else v-for="(skillset, count) in skills" :key="count">
                <div class="skill-type"><p>{{ skillset.type }}</p></div>
                <div class="skill-description"><p>{{ skillset.description }}</p></div>
                <div class="skill-options">
                  <div class="skill-option edit-skill"><i class="fas fa-pen" @click="editSkill(count)"></i><div class="hint"><p>Edit</p></div></div>
                  <div class="skill-option delete-skill"><i class="fas fa-trash" @click="deleteSkill(count)"></i><div class="hint"><p>Delete</p></div></div>
                </div>
              </div>
            </div>
            <div class="profile-modal-title">
              <div class="profile-modal-title-inner">
                <p>Career History</p>
              </div>
              <div class="add-skill-button">
                <p @click="openCareerModal"><i class="fas fa-plus"></i> Add career step</p>
              </div>
            </div>
            <div id="career-history">
              <div class="no-career" v-if="career_steps.length == 0">
                <p>You have not added any Career step. Click on Add Step button to add a Career Step</p>
              </div>
              <div class="career-step" v-else v-for="(step, count) in career_steps" :key="count">
                <div class="step-title">
                  <p class="step-organisation">{{ step.organisation_name }}</p>
                  <br>
                  <p class="step-duration"><span>{{ step.position }} </span><span class="step-duration-step">( {{ step.from }} - {{ step.to }} )</span></p>
                  <div class="skill-options">
                    <div class="skill-option edit-skill"><i class="fas fa-pen" @click="editCareer(count)"></i><div class="hint"><p>Edit</p></div></div>
                    <div class="skill-option delete-skill"><i class="fas fa-trash" @click="deleteCareer(count)"></i><div class="hint"><p>Delete</p></div></div>
                  </div>
                </div>
                <ul class="step-list">
                  <li v-for="(achievement, count) in step.achievements" :key="count">{{ achievement.data }}</li>
                </ul>
              </div>
            </div>
            <div class="profile-modal-title">
              <div class="profile-modal-title-inner">
                <p>Education Details</p>
              </div>
              <div class="add-skill-button">
                <p @click="openEducationModal"><i class="fas fa-plus"></i> Add Education</p>
              </div>
            </div>
            <ul id="education-details">
              <li class="education-step" v-for="(education, count) in educations" :key="count">
                <span class="course-name">{{ education.course_name }}</span> - <span class="institute-name">{{ education.institute }}</span> - <span class="course-duration">{{ education.from }} to {{ education.to }}</span> - <span class="course-marks">{{ education.score }}</span>
                <div class="skill-options">
                  <div class="skill-option edit-skill"><i class="fas fa-pen" @click="editEducation(count)"></i><div class="hint"><p>Edit</p></div></div>
                  <div class="skill-option delete-skill"><i class="fas fa-trash" @click="deleteEducation(count)"></i><div class="hint"><p>Delete</p></div></div>
                </div>
              </li>
            </ul>
            <div class="profile-modal-title">
              <div class="profile-modal-title-inner">
                <p>Social Profiles</p>
              </div>
            </div>
            <ul class="profile-basics social-profiles">
              <div class="fields">
                <div class="field"><i class="fab fa-facebook-f"></i><input type="text" v-model="facebook" placeholder="Facebook Profile" @input="refreshSave" /></div>
                <div class="field"><i class="fab fa-twitter"></i><input type="text" v-model="twitter" placeholder="Twitter Profile" @input="refreshSave" /></div>
                <div class="field"><i class="fab fa-reddit-alien"></i><input type="text" v-model="reddit" placeholder="Reddit Profile" @input="refreshSave" /></div>
                <div class="field"><i class="fab fa-linkedin-in"></i><input type="text" v-model="linkedin" placeholder="Linkedin Profile" @input="refreshSave" /></div>
                <div class="field"><i class="fab fa-github"></i><input type="text" v-model="github" placeholder="Github Profile" @input="refreshSave" /></div>
                <div class="field"><i class="fab fa-youtube"></i><input type="text" v-model="youtube" placeholder="YouTube Channel" @input="refreshSave" /></div>
              </div>
            </ul>
          </div>
          <div id="profile-footer">
            <div id="profile-footer-inner">
              <div class="cancel-button">
                <p @click="closeModal"><i class="fas fa-times"></i>Close</p>
              </div>
              <div class="save-button">
                <!--<p v-if="save_data_enable" @click="saveData">Save<i class="fas fa-save"></i></p>
                <p v-else class="disable">Save<i class="fas fa-save"></i></p>-->
                <p @click="saveData">Save<i class="fas fa-save"></i></p>
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
  #profile-modal{
    .modal-title{border-bottom: 1px solid #eee;}
    .sk-circle{width: 30px;height: 30px;}
    .modal-box{padding: 15px 0;padding-top: 45px;height: 540px;position: relative;
      .sub-modal-title{font-size: 12px;font-weight: 600;line-height: 36px;padding: 0 12px;color: #333;text-align: left;border-bottom: 1px solid #eee;}
      #image-cropper{position: absolute;top: 0;left: 0;width: 100%;height: 100%;z-index: 10;
        canvas{display: block !important;}
      }
      textarea, input{letter-spacing: 0.4px;color: #34495E;}
      textarea{line-height: 16px;}
      #skill-editor, #career-editor, #education-editor{position: absolute;top: 0;left: 0;width: 100%;height: 100%;background-color: rgba(0,0,0,0.5);z-index: 5;transition: 250ms;
        .inner-editor-vertical{display: table-cell;vertical-align: middle;}
        .inner-editor-inner{width: 60%;margin: 0 auto;background-color: #fff;border-radius: 5px;overflow: hidden;transition: 250ms;}
        .sub-modal-body{padding: 12px 12px;max-height: 306px;overflow-y: auto;}
        .sub-modal-buttons{padding: 6px 15px;border-top: 1px solid #eee;
          .button{float: left;text-align: center;font-size: 11px;font-weight: 600;color: #f6f6f6;transition: 250ms;cursor: pointer;line-height: 32px;
            p{line-height: 28px;padding: 0 10px;transition: 150ms;cursor: pointer;font-size: 12px;font-weight: 600;border-radius: 4px;color: #f6f6f6;}
            &.cancel{text-align: left;
              p{background-color: #E74C3C;
                i{margin-right: 5px;}
                &:hover{background-color: #C0392B;}
              }
            }
            &.save{text-align: right;
              p{background-color: #2ECC71;
                i{margin-left: 5px;}
                &:hover{background-color: #27AE60;}
              }
            }
            &:first-child{float: left;}
            &:last-child{float: right;}
          }
          &:after{clear: both;display: block;content: "";}
        }
        .fields-row{margin: 0 -5px;
          &:after{clear: both;display: block;content: "";}
        }
        .input-field{
          &.col{width: 50%;float: left;padding: 0 5px;box-sizing: border-box;}
          input{width: 100%;height: 32px;background-color: #eee;padding: 0 10px;box-sizing: border-box;border-radius: 4px;font-size: 12px;font-weight: 600;background-color: #fff;margin-bottom: 6px;background-color: #f6f6f6;border: 1px solid #eee;}
          &.half{}
        }
        .textarea-field{
          textarea{width: 100%;height: 120px;resize: none;background-color: #f6f6f6;padding: 10px;box-sizing: border-box;font-weight: 600;border-radius: 4px;border: 1px solid #eee;font-size: 12px;vertical-align: middle;}
          &.achievement{
            .achievement-row{margin-bottom: 0px;
              label{float: left;line-height: 16px;}
              .achievement-delete{float: right;line-height: 18px;
                i{color: red;font-size: 12px;line-height: 10px;cursor: pointer;}
              }
              &:after{clear: both;display: block;content: "";}
            }
            textarea{height: 100px;}
          }
        }
        .input-field, .textarea-field{
          label{font-size: 11px;font-weight: 600;margin-left: 5px;}
        }
        &.closed{display: none;opacity: 0;
          .inner-editor-inner{transform: scale(0.8);}
        }
        &.opening{display: table;opacity: 0;
          .inner-editor-inner{transform: scale(0.8);}
        }
        &.opened{display: table;opacity: 1;
          .inner-editor-inner{transform: scale(1);}
        }
      }
      #career-editor{
        #add-temp-achievement{text-align: center;margin-top: 6px;
          #add-temp-achievement-inner{display: inline-block;
            p{font-size: 11px;color: #eee;border-radius: 4px;font-weight: 600;padding: 2px 10px;background-color: #3d3d3d;cursor: pointer;
              i{margin-right: 3px;}
            }
          }
        }
      }
      #profile-modal-loader{position: absolute;top: 0;left: 0;top: 0;left: 0;width: 100%;height: 100%;background-color: rgba(0,0,0,0.5);z-index: 5;display: table;transition: 250ms;
        &.closed{display: none;opacity: 0;}
        &.opening{display: block;opacity: 0;}
        &.opened{display: table;opacity: 1;}
        #profile-modal-loader-inner{display: table-cell;vertical-align: middle;}
      }
      .profile-image{float: left;width: 184px;position: relative;
        img{border-radius: 4px;box-shadow: -2px 2px 5px 0 rgba(0,0,0,0.15);width: 184px;height: 184px;vertical-align: middle;}
        #edit-picture{position: absolute;top: 0;left: 0;width: 100%;height: 100%;z-index: 2;background-color: transparent;transition: 250ms;display: table;opacity: 0;cursor: pointer;
          #edit-picture-vertical{display: table-cell;vertical-align: middle;text-align: center;
            p, i{color: #fff;}
            p{font-size: 12px;font-weight: 600;}
          }
        }
        &:hover{
          #edit-picture{background-color: rgba(0,0,0,0.5);opacity: 1;}
        }
      }
      .profile-basics{float: left;width: calc(100% - 184px);padding: 0 15px;box-sizing: border-box;
        &.social-profiles{width: 100%;padding: 0;margin: 4px -8px 0px -8px;
          .field{float: left;width: 50% !important;
            i{color: #fff !important;}
            input{width: calc(100% - 30px) !important;font-size: 11px !important;}
            .fa-facebook-f{background-color: #3b5998 !important;}
            .fa-twitter{background-color: #1da1f2 !important;}
            .fa-reddit-alien{background-color: #ff4500 !important;}
            .fa-linkedin-in{background-color: #0077b5 !important;}
            .fa-github{background-color: #333 !important;}
            .fa-youtube{background-color: #ff0000 !important;}
          }
        }
      }
      #profile-tabs{position: absolute;top: 38px;left: 0;width: 100%;padding: 0 15px;box-sizing: border-box;display: none;
        .tabs-col{width: 33.33%;float: left;
          .tab{text-align: center;background-color: #1ABC9C;line-height: 26px;border-right: 1px solid darken(#1ABC9C, 4%);cursor: pointer;transition: 150ms;
            p{font-size: 11px;font-weight: 600;
              i{font-size: 0.9em;margin-right: 4px;}
            }
            p, i{vertical-align: middle;color: #f6f6f6;}
            &:hover{background-color: #16A085;}
          }
          &:first-child{
            .tab{border-radius: 4px 0 0 4px;}
          }
          &:last-child{border-right: 0;
            .tab{border-radius: 0 4px 4px 0;}
          }
        }
      }
      #profile-footer{position: absolute;bottom: 0;left: 0;width: 100%;box-sizing: border-box;background-color: #fff;padding: 6px 15px;border-top: 1px solid #eee;border-radius: 0 0 5px 5px;
        .cancel-button{float: left;
          p{background-color: #E74C3C;
            i{margin-right: 5px;}
            &:hover{background-color: #C0392B;}
          }
        }
        .save-button{float: right;
          p{background-color: #2ECC71;
            i{margin-left: 5px;}
            &.disable{background-color: #eee;color: #bbb;cursor: default;
              &:hover{background-color: #eee;color: #bbb;}
            }
            &:hover{background-color: #27AE60;}
          }
        }
        p{line-height: 28px;padding: 0 10px;transition: 150ms;cursor: pointer;font-size: 12px;font-weight: 600;border-radius: 4px;color: #f6f6f6;}
        &:after{clear: both;display: block;content: "";}
      }
      #profile-main-content{position: absolute;top: 41px;width: 100%;height: calc(100% - 82px);overflow-y: auto;padding: 10px 20px;box-sizing: border-box;
        #profile-basic-info{
          input[type='file']{display: none;}
          &:after{clear: both;display: block;content: "";}
        }
        .profile-basics, #profile-basic-info{
          .fields{
            .field{width: 100%;padding: 0 10px;box-sizing: border-box;
              i{width: 30px;float: left;text-align: center;line-height: 32px;border-right: 0;box-sizing: border-box;font-size: 12px;border-radius: 4px 0 0 4px;background-color: #eee;color: #555;}
              input{width: calc(95% - 30px);height: 32px;background-color: #eee;padding: 0 10px;box-sizing: border-box;border-radius: 0 4px 4px 0;font-size: 12px;font-weight: 600;background-color: #fff;margin-bottom: 6px;border-left: 0;background-color: #f6f6f6;border: 1px solid #eee;border-left: 0;}
              &:last-child{
                input{margin-bottom: 0;}
              }
            }
            &:after{clear: both;display: block;content: "";}
          }
        }
        .short-summary{margin-top: 2px;
          label{font-size: 12px;}
          textarea{width: 100%;height: 100px;resize: none;background-color: #f6f6f6;padding: 10px;box-sizing: border-box;font-weight: 500;border-radius: 4px;border: 1px solid #eee;font-size: 12px;}
        }
        .profile-modal-title{font-size: 16px;font-weight:500;margin-top: 12px;
          &:after{clear: both;display: block;content: "";}
        }
        #education-details{margin-left: 21px;
          .education-step{padding: 4px 30px 4px 6px;list-style-type: disc;position: relative;border-bottom: 1px solid #eee;color: #34495E;font-size: 10px;margin-left: 1px;padding-left: 7px;
            .course-name{font-weight: 600;margin-right: 4px;margin-left: -6px;}
            .institute-name{font-weight: 600;margin-right: 4px;}
            .course-duration{margin-right: 4px;font-weight: 600;color: #16A085;}
            .course-marks{font-weight: 600;color: #7F8C8D;}
            &:last-child{border-bottom: 0;}
          }
        }
        .profile-modal-title-inner{float: left;}
        .add-skill-button{background-color: #2ECC71;float: left;margin: 4px 8px;padding: 0 5px;border-radius: 4px;font-weight: 600;cursor: pointer;transition: 150ms;
          i{margin-left: 1px;}
          p, i{color: #f6f6f6;font-size: 10px;margin-right: 1px;line-height: 16px;vertical-align: middle;}
          &:hover{background-color: #27AE60;}
        }
        #profile-skills{
          .no-skills{font-size: 10px;font-weight: 600;color: #7F8C8D;padding: 0 3px;margin-top: 3px;}
          .profile-skill{margin: 5px -5px;border-bottom: 1px solid #eee;padding-bottom: 4px;padding-top: 4px;width: 100%;position: relative;
            .skill-type{width: 30%;
              p{font-weight: 600;}
            }
            .skill-description{
              p{font-size: 10px;font-weight: 500;color: #34495E;}
            }
            .skill-type, .skill-description{float: left;padding: 0 10px;box-sizing: border-box;}
            .skill-description{width: 70%;padding-right: 45px;}
            p{font-size: 11px;}
            &:after{clear: both;display: block;content: "";}
            &:last-child{border-bottom: 0;}
          }
        }
        .skill-options{position: absolute;top: 0px;right: 0px;
          .skill-option{float: left;margin-right: 8px;position: relative;
            i{font-size: 11px;line-height: 17px;vertical-align: middle;margin-bottom: 4px;}
            &:last-child{margin-right: 0;}
            i{transition: 150ms;cursor: pointer;
              &:hover + .hint{opacity: 1;transform: scale(1) translate(0px, 0px);}
            }
            &.edit-skill{
              .hint{right: -8px;
                &:after{left: 12px;}
              }
              i{color: #3498DB;}
              &:hover{
                i{color: #2980B9;}
              }
            }
            &.delete-skill{
              i{color: #E74C3C;}
              &:hover{
                i{color: #C0392B;}
              }
            }
            .hint{position: absolute;top: -18px;right: -15px;opacity: 0;transition: 150ms;transform: scale(0.6) translate(4px, 16px);
              p{background-color: #444;color: #f6f6f6;font-weight: 600;padding: 1px 5px;font-size: 10px;border-radius: 3px;}
              &:after{display: block;content: "";height: 5px;width: 5px;position: absolute;top: 15px;left: 21px;background: #444;transform: rotate(45deg);}
            }
          }
          &:after{clear: both;display: block;content: "";}
        }
        #career-history{
          .no-career{font-size: 10px;font-weight: 600;color: #7F8C8D;padding: 0 3px;margin-top: 3px;}
          .career-step{padding: 0 3px 3px 3px;margin-top: 8px;border-bottom: 1px solid #eee;
            .step-title{position: relative;
              .step-organisation{float: left;font-weight: 600;font-size: 14px;}
              .step-duration{float: left;font-size: 10px;font-weight: 600;margin-left: 5px;vertical-align: bottom;line-height: 10px;margin-top: 7px;
                .step-duration-step{color: #16A085;margin-left: 2px;}
              }
              &:after{clear: both;display: block;content: "";}
            }
            .step-list{margin-left: 12px;padding-left: 7px;position: relative;padding-top: 3px;
              li{font-size: 10px;padding: 3px 0 3px 0;position: relative;font-weight: 500;color: #34495E;list-style-type: disc;
                //&:after{content: "";display: block;position: absolute;height: 2px;background-color: #333;top: 10px;left: -8px;width: 6px;}
              }
              &:after{display: block;content: "";position: absolute;left: 10px;bottom: 10px;height: 30px;width: 2px;background-color: #fff;left: -3px;bottom: 0px;height: 26px;width: 4px;}
            }
            &:last-child{border-bottom: 0;}
            &:after{clear: both;display: block;content: "";}
          }
        }
      }
    }
  }
</style>

<script>
import Loading from '@/components/common/Loading'
// import ImageCropper from '@/components/common/ImageCropper'
import axios from 'axios'
export default {
  name: 'Profile',
  props: { status: String },
  components: {
    Loading //, ImageCropper
  },
  computed: {
    computedStatus: function () { return 'modal ' + this.$props.status },
    profile_picture: function () { return 'https://api.markmycv.com//api/image/' + this.$data.hashcode }
  },
  data () {
    return { fullname: '', position: '', location: '', email_id: '', contact_no: '', summary: '', temp_skill_header: '', hashcode: '', temp_skill_description: '', skills: [], temp_skill_title: '', temp_career_title: '', temp_organisation_name: '', temp_position: '', temp_duration_start: '', temp_duration_end: '', temp_achievements: [], skill_to_edit: 0, modal_loader: 'closed', career_steps: [], skill_editor_class: 'closed', career_editor_class: 'closed', career_to_edit: 0, education_to_edit: 0, education_editor_class: 'closed', temp_education_title: '', temp_course_name: '', temp_institute_name: '', temp_education_start: '', temp_education_end: '', temp_education_score: '', educations: [], facebook: '', twitter: '', reddit: '', linkedin: '', github: '', youtube: '', save_data_enable: false, temp: [], core_skills: '', objective: '' }
  },
  created () {
    let data = this.$data
    let emitter = this
    let access = 'Bearer ' + window.localStorage.getItem('access')
    if (access !== 'Bearer null') {
      axios({
        method: 'post',
        url: 'https://api.markmycv.com//api/get-profile',
        headers: {
          Authorization: access
        },
        data: { }
      }).then(function (response) {
        let bkup = JSON.parse(response.data.data)
        if (bkup !== null) {
          data.hashcode = bkup.hashcode
          data.fullname = bkup.fullname
          data.position = bkup.position
          data.location = bkup.location
          data.email_id = bkup.email_id
          data.contact_no = bkup.contact_no
          data.summary = bkup.summary
          data.objective = bkup.objective
          data.core_skills = bkup.core_skills
          data.facebook = bkup.facebook
          data.twitter = bkup.twitter
          data.reddit = bkup.reddit
          data.linkedin = bkup.linkedin
          data.github = bkup.github
          data.youtube = bkup.youtube
          data.skills = bkup.skills
          data.career_steps = bkup.career_steps
          data.educations = bkup.educations
          emitter.$emit('profile', data.hashcode, data.fullname, data.email_id)
        }
        data.temp.fullname = data.fullname
        data.temp.position = data.position
        data.temp.location = data.location
        data.temp.email_id = data.email_id
        data.temp.contact_no = data.contact_no
        data.temp.summary = data.summary
        data.temp.objective = data.objective
        data.temp.core_skills = data.core_skills
        data.temp.facebook = data.facebook
        data.temp.twitter = data.twitter
        data.temp.reddit = data.reddit
        data.temp.linkedin = data.linkedin
        data.temp.github = data.github
        data.temp.youtube = data.youtube
        data.temp.skills = data.skills
        data.temp.career_steps = data.career_steps
      }).catch(function (error) {
        console.log(error)
      }).finally(function () { })
    }
  },
  watch: {
    data: function () {
      console.log('Changed data')
    }
  },
  methods: {
    saveData () {
      let data = this.$data
      let emitter = this
      data.modal_loader = 'opening'
      setTimeout(function () {
        data.modal_loader = 'opened'
      }, 10)
      let access = 'Bearer ' + window.localStorage.getItem('access')
      let saveData = {}
      saveData['hashcode'] = data.hashcode
      saveData['fullname'] = data.fullname
      saveData['position'] = data.position
      saveData['location'] = data.location
      saveData['email_id'] = data.email_id
      saveData['contact_no'] = data.contact_no
      saveData['summary'] = data.summary
      saveData['objective'] = data.objective
      saveData['core_skills'] = data.core_skills
      saveData['facebook'] = data.facebook
      saveData['twitter'] = data.twitter
      saveData['reddit'] = data.reddit
      saveData['linkedin'] = data.linkedin
      saveData['github'] = data.github
      saveData['youtube'] = data.youtube
      saveData['skills'] = data.skills
      saveData['career_steps'] = data.career_steps
      saveData['educations'] = data.educations
      axios({
        method: 'post',
        url: 'https://api.markmycv.com//api/save-profile',
        headers: {
          Authorization: access
        },
        data: {
          data: JSON.stringify(saveData)
        }
      }).then(function (response) {
        if (response.data.status === 'ok') {
          data.modal_loader = 'opening'
          setTimeout(function () {
            data.modal_loader = 'closed'
            data.temp.fullname = data.fullname
            data.temp.position = data.position
            data.temp.location = data.location
            data.temp.email_id = data.email_id
            data.temp.contact_no = data.contact_no
            data.temp.summary = data.summary
            data.temp.objective = data.objective
            data.temp.core_skills = data.core_skills
            data.temp.facebook = data.facebook
            data.temp.twitter = data.twitter
            data.temp.reddit = data.reddit
            data.temp.linkedin = data.linkedin
            data.temp.github = data.github
            data.temp.youtube = data.youtube
            data.temp.skills = data.skills
            data.temp.career_steps = data.career_steps
          }, 260)
          emitter.$emit('profile', data.hashcode, data.fullname, data.email_id)
          emitter.closeModal()
        }
      }).catch(function (error) {
        console.log(error)
      }).finally(function () { })
    },
    onImageChange (e) {
      // const file = e.target.files[0]
      const url = 'https://api.markmycv.com//api/upload-profile-pic'
      let target = this.$data
      let data = new FormData()
      data.append('name', e.target.files[0])
      data.append('file', event.target.files[0])
      let config = {
        header: {
          'Content-Type': 'image/jpg'
        }
      }
      axios.post(
        url,
        data,
        config
      ).then(
        response => {
          target.hashcode = response.data.hashcode
        }
      )
    },
    openSkillModal () {
      let data = this.$data
      data.temp_skill_title = 'Add Skillset'
      data.skill_editor_class = 'opening'
      setTimeout(function () {
        data.skill_editor_class = 'opened'
      }, 10)
    },
    addSkill () {
      let data = this.$data
      let tempArr = {}
      tempArr.type = data.temp_skill_header
      tempArr.description = data.temp_skill_description
      data.skills.push(tempArr)
      data.skill_editor_class = 'opening'
      setTimeout(function () {
        data.skill_editor_class = 'closed'
        data.temp_skill_header = ''
        data.temp_skill_description = ''
      }, 260)
    },
    editSkill (count) {
      let data = this.$data
      data.temp_skill_title = 'Edit Skillset'
      data.temp_skill_header = data.skills[count].type
      data.temp_skill_description = data.skills[count].description
      data.skill_to_edit = count
      data.skill_editor_class = 'opening'
      setTimeout(function () {
        data.skill_editor_class = 'opened'
        this.refreshSave()
      }, 10)
    },
    saveEditSkill () {
      let data = this.$data
      data.skills[data.skill_to_edit].type = data.temp_skill_header
      data.skills[data.skill_to_edit].description = data.temp_skill_description
      data.skill_editor_class = 'opening'
      setTimeout(function () {
        data.skill_editor_class = 'closed'
        data.temp_skill_header = ''
        data.temp_skill_description = ''
        this.refreshSave()
      }, 260)
    },
    deleteSkill (count) {
      this.$data.skills.splice(count, 1)
    },
    cancelSkill () {
      let data = this.$data
      data.skill_editor_class = 'opening'
      setTimeout(function () {
        data.skill_editor_class = 'closed'
        data.temp_skill_header = ''
        data.temp_skill_description = ''
      }, 260)
    },
    openCareerModal () {
      let data = this.$data
      data.temp_career_title = 'Add Career Step'
      data.career_editor_class = 'opening'
      setTimeout(function () {
        data.career_editor_class = 'opened'
      }, 10)
    },
    cancelCareer () {
      let data = this.$data
      data.career_editor_class = 'opening'
      setTimeout(function () {
        data.career_editor_class = 'closed'
        data.temp_organisation_name = ''
        data.temp_duration_start = ''
        data.temp_duration_end = ''
        data.temp_achievements = []
      }, 260)
    },
    addCareer () {
      let data = this.$data
      let tempArr = {}
      tempArr.organisation_name = data.temp_organisation_name
      tempArr.position = data.temp_position
      tempArr.from = data.temp_duration_start
      tempArr.to = data.temp_duration_end
      tempArr.achievements = data.temp_achievements
      data.career_steps.push(tempArr)
      data.career_editor_class = 'opening'
      setTimeout(function () {
        data.career_editor_class = 'closed'
        data.temp_career_title = ''
        data.temp_organisation_name = ''
        data.temp_position = ''
        data.temp_duration_start = ''
        data.temp_duration_end = ''
        data.temp_achievements = []
        this.refreshSave()
      }, 260)
    },
    editCareer (count) {
      let data = this.$data
      data.temp_career_title = 'Edit Career Step'
      data.temp_organisation_name = data.career_steps[count].organisation_name
      data.temp_position = data.career_steps[count].position
      data.temp_duration_start = data.career_steps[count].from
      data.temp_duration_end = data.career_steps[count].to
      data.temp_achievements = data.career_steps[count].achievements
      data.career_to_edit = count
      data.career_editor_class = 'opening'
      setTimeout(function () {
        data.career_editor_class = 'opened'
      }, 10)
    },
    saveEditCareer () {
      let data = this.$data
      data.career_steps[data.career_to_edit].organisation_name = data.temp_organisation_name
      data.career_steps[data.career_to_edit].position = data.temp_position
      data.career_steps[data.career_to_edit].from = data.temp_duration_start
      data.career_steps[data.career_to_edit].to = data.temp_duration_end
      data.career_steps[data.career_to_edit].achievements = data.temp_achievements
      data.career_editor_class = 'opening'
      setTimeout(function () {
        data.career_editor_class = 'closed'
        data.temp_organisation_name = ''
        data.temp_duration_start = ''
        data.temp_duration_end = ''
        data.temp_achievements = []
        this.refreshSave()
      }, 260)
    },
    deleteCareer (count) {
      this.$data.career_steps.splice(count, 1)
    },
    addAchievement () {
      let data = this.$data
      data.temp_achievements.push({ data: '' })
    },
    openEducationModal () {
      let data = this.$data
      data.education_editor_class = 'opening'
      data.temp_education_title = 'Add Education'
      setTimeout(function () {
        data.education_editor_class = 'opened'
      }, 10)
    },
    addEducation () {
      let data = this.$data
      let tempArr = {}
      tempArr.course_name = data.temp_course_name
      tempArr.institute = data.temp_institute_name
      tempArr.from = data.temp_education_start
      tempArr.to = data.temp_education_end
      tempArr.score = data.temp_education_score
      data.educations.push(tempArr)
      data.education_editor_class = 'opening'
      setTimeout(function () {
        data.temp_education_title = ''
        data.temp_course_name = ''
        data.temp_institute_name = ''
        data.temp_education_start = ''
        data.temp_education_end = ''
        data.temp_education_score = ''
        data.education_editor_class = 'closed'
        this.refreshSave()
      }, 260)
    },
    editEducation (count) {
      let data = this.$data
      data.temp_education_title = 'Edit Education'
      data.temp_course_name = data.educations[count].course_name
      data.temp_institute_name = data.educations[count].institute
      data.temp_education_start = data.educations[count].from
      data.temp_education_end = data.educations[count].to
      data.temp_education_score = data.educations[count].score
      data.education_to_edit = count
      data.education_editor_class = 'opening'
      setTimeout(function () {
        data.education_editor_class = 'opened'
      }, 10)
    },
    saveEditEducation () {
      let data = this.$data
      data.educations[data.education_to_edit].course_name = data.temp_course_name
      data.educations[data.education_to_edit].institute = data.temp_institute_name
      data.educations[data.education_to_edit].from = data.temp_education_start
      data.educations[data.education_to_edit].to = data.temp_education_end
      data.educations[data.education_to_edit].score = data.temp_education_score
      data.education_editor_class = 'opening'
      setTimeout(function () {
        data.education_editor_class = 'closed'
        data.temp_course_name = ''
        data.temp_institute_name = ''
        data.temp_education_start = ''
        data.temp_education_end = []
        data.temp_education_score = ''
        this.refreshSave()
      }, 260)
    },
    deleteEducation (count) {
      this.$data.educations.splice(count, 1)
      this.refreshSave()
    },
    cancelEducation () {
      let data = this.$data
      data.education_editor_class = 'opening'
      setTimeout(function () {
        data.temp_education_title = 'Edit Education'
        data.temp_course_name = ''
        data.temp_institute_name = ''
        data.temp_education_start = ''
        data.temp_education_end = ''
        data.temp_education_score = ''
        data.education_editor_class = 'closed'
      }, 260)
    },
    refreshSave () {
      console.log('refreshSave')
      let data = this.$data
      if (
        data.temp.hashcode !== data.hashcode ||
        data.temp.fullname !== data.fullname ||
        data.temp.position !== data.position ||
        data.temp.location !== data.location ||
        data.temp.email_id !== data.email_id ||
        data.temp.contact_no !== data.contact_no ||
        data.temp.summary !== data.summary ||
        data.temp.objective !== data.objective ||
        data.temp.core_skills !== data.core_skills ||
        data.temp.facebook !== data.facebook ||
        data.temp.twitter !== data.twitter ||
        data.temp.reddit !== data.reddit ||
        data.temp.linkedin !== data.linkedin ||
        data.temp.github !== data.github ||
        data.temp.youtube !== data.youtube ||
        data.temp.skills !== data.skills ||
        data.temp.career_steps !== data.career_steps
      ) {
        data.save_data_enable = true
      } else {
        data.save_data_enable = false
      }
    },
    closeModal () { this.$emit('closeProfileModal') }
  }
}
</script>
