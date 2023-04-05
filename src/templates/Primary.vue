<template>
  <div>
    <Nav @login="login_username" @closeHome="closeHome" />
    <div id="templates-background" :class="background_status"></div>
    <div id="background-overlay" :class="overlay_class"></div>
    <div id="template-editor">
      <div id="resume-editor">
           <!--<div id="resume-editor-banner">
             <div id="resume-editor-banner-inner">
               <div id="resume-editor-banner-vertical">
                 <p class="title">Fill the fields below</p>
                 <hr>
                 <p class="content">Watch for changes while filling out data</p>
               </div>
             </div>
           </div>-->
           <div id="resume-editor-title">
           </div>
           <div class="fields-section">
              <div class="fields-section-title">
                 <p>Basic Information</p>
              </div>
              <div class="fields-section-content">
                 <div class="special-field-wrapper field">
                  <div class="special-field-card">
                    <div class="special-icon">
                       <i class="fas fa-user"></i>
                    </div>
                    <div class="special-field">
                       <label> Full name</label>
                       <input placeholder="Enter full name" type="text" v-model="fullname" />
                    </div>
                  </div>
                 </div>
                 <div class="special-field-wrapper field">
                  <div class="special-field-card">
                    <div class="special-icon">
                       <i class="fas fa-crosshairs"></i>
                    </div>
                    <div class="special-field">
                       <label> Position</label>
                       <input placeholder="Enter position" type="text" v-model="position" />
                    </div>
                  </div>
                 </div>
              </div>
           </div>
           <div class="fields-section">
              <div class="fields-section-title">
                 <p>Contact Information</p>
              </div>
              <div class="fields-section-hint">
                 <div class="field-hint-inner">
                  <p>Providing contact information is very important to include in a CV as it allows a recruiter to contact you in case he/she gains interest in your Profile. Some CVs lack the contact details, which leaves the recruiter in a condition to look for you on the Internet or search for you Offline to contact you. Location informs the recruiter if you are present in the same state/city as the recruiter's office or in a different one. Email ID and Contact No. allows recruiter to contact you directly and proceed.</p>
                </div>
              </div>
              <div class="fields-section-content">
                <div class="special-field-wrapper field">
                  <div class="special-field-card">
                    <div class="special-icon">
                      <i class="fas fa-map-marker-alt"></i>
                    </div>
                    <div class="special-field">
                      <label> Current Location</label>
                      <input placeholder="Enter current location" type="text" v-model="location" />
                    </div>
                  </div>
                 </div>
                 <div class="special-field-wrapper field">
                  <div class="special-field-card">
                    <div class="special-icon">
                       <i class="fas fa-envelope"></i>
                    </div>
                    <div class="special-field">
                       <label> Email ID</label>
                       <input placeholder="Enter Email ID" type="text" v-model="emailid" />
                    </div>
                  </div>
                 </div>
                 <div class="special-field-wrapper field">
                  <div class="special-field-card">
                    <div class="special-icon">
                       <i class="fas fa-phone"></i>
                    </div>
                    <div class="special-field">
                       <label> Contact No.</label>
                       <input placeholder="Enter Mobile No." type="text" v-model="phone" />
                    </div>
                 </div>
               </div>
              </div>
           </div>
           <div class="fields-section">
              <div class="fields-section-title">
                 <p>Social Profiles</p>
              </div>
              <div class="fields-section-hint">
                 <div class="field-hint-inner">
                  <p>Providing the links to your Social Networking Profiles or Portfolios is important for recruiter to check your online activeness and analyse your networks.</p>
                </div>
              </div>
              <div class="fields-section-content">
                 <div class="special-field-wrapper field">
                  <div class="special-field-card">
                    <div class="special-icon social-icon">
                       <i class="fab fa-github-square"></i>
                    </div>
                    <div class="special-field">
                       <label> Github Profile</label>
                       <input placeholder="Enter Github URL" type="text" v-model="github" />
                    </div>
                  </div>
                 </div>
                 <div class="special-field-wrapper field">
                  <div class="special-field-card">
                    <div class="special-icon social-icon">
                       <i class="fab fa-facebook-square"></i>
                    </div>
                    <div class="special-field">
                       <label> Facebook Profile</label>
                       <input placeholder="Enter Facebook URL" type="text" v-model="facebook" />
                    </div>
                  </div>
                 </div>
                 <div class="special-field-wrapper field">
                  <div class="special-field-card">
                    <div class="special-icon social-icon">
                       <i class="fab fa-reddit-square"></i>
                    </div>
                    <div class="special-field">
                       <label> Reddit Profile</label>
                       <input placeholder="Enter Reddit URL" type="text" v-model="reddit" />
                    </div>
                  </div>
                 </div>
                 <div class="special-field-wrapper field">
                  <div class="special-field-card">
                    <div class="special-icon social-icon">
                       <i class="fab fa-twitter-square"></i>
                    </div>
                    <div class="special-field">
                       <label> Twitter Profile</label>
                       <input placeholder="Enter Twitter URL" type="text" v-model="twitter" />
                    </div>
                  </div>
                 </div>
                 <div class="special-field-wrapper field">
                  <div class="special-field-card">
                    <div class="special-icon social-icon">
                       <i class="fab fa-linkedin"></i>
                    </div>
                    <div class="special-field">
                       <label> Linkedin Profile</label>
                       <input placeholder="Enter Linkedin URL" type="text" v-model="linkedin" />
                    </div>
                  </div>
                 </div>
                 <div class="special-field-wrapper field">
                  <div class="special-field-card">
                    <div class="special-icon social-icon">
                       <i class="fab fa-behance-square"></i>
                    </div>
                    <div class="special-field">
                       <label> Behance Profile</label>
                       <input placeholder="Enter Behance URL" type="text" v-model="behance" />
                    </div>
                  </div>
                 </div>
                 <div class="special-field-wrapper field">
                  <div class="special-field-card">
                    <div class="special-icon social-icon">
                       <i class="fab fa-youtube"></i>
                    </div>
                    <div class="special-field">
                       <label> YouTube Channel</label>
                       <input placeholder="Enter YouTube URL" type="text" v-model="youtube" />
                    </div>
                  </div>
                 </div>
              </div>
           </div>
          <div class="fields-section">
              <div class="fields-section-title">
                 <p>Professional Summary</p>
              </div>
              <div class="fields-section-hint">
                 <div class="field-hint-inner">
                  <p>Include a short professional statement at the top of your resume. This section provides quick context for employers as they review your application.</p>
                </div>
              </div>
              <div class="fields-section-content --textarea-section">
                 <div class="fields">
                  <div class="full-field --full-field achievement-textarea">
                    <label>Summary</label>
                    <textarea placeholder="Enter your achievement here" v-model="summary" />
                  </div>
                </div>
              </div>
           </div>
           <div class="fields-section">
              <div class="fields-section-title">
                 <p>Skills</p>
              </div>
              <div class="fields-section-hint">
                <div class="field-hint-inner">
                 <p>Your skills and abilities section should highlight your most relevant competencies.</p>
                  <ul>
                    <li>Skills and abilities can include both hard (technical) skills and soft (interpersonal) skills.</li>
                    <li>The most important consideration when listing your skills whether or not they are relevant to the job.</li>
                    <li>Carefully review the job posting to identify which of your skills the employer is looking for in an ideal candidate and include them in your skills section.</li>
                  </ul>
               </div>
              </div>
              <div class="fields-section-content --textarea-section">
                <div class="fields education-course" v-for="(skill, count) in skills" :key="count">
                  <div class="section-sub-title">
                    <p>Enter skill {{ count + 1 }} details</p>
                    <div class="cancel-career-step" @click="deleteskill(count)"><i class="fas fa-times"></i></div>
                  </div>
                  <div class="field skill-name">
                    <label>Skill name</label>
                    <input placeholder="Enter skill name" type="text" v-model="skill.type">
                  </div>
                  <div class="field skill-description">
                    <label>Skill description</label>
                    <input placeholder="Enter skill description" type="text" v-model="skill.description">
                  </div>
                </div>
                <div class="add-education-step">
                  <div class="add-education-step-inner">
                    <p @click="addskill"><i class="fas fa-plus-circle"></i> Add skill</p>
                  </div>
                </div>
              </div>
           </div>
           <div class="fields-section">
              <div class="fields-section-title">
                 <p>Profile Picture</p>
              </div>
              <div class="fields-section-hint">
                 <div class="field-hint-inner">
                  <p>Basic information just includes your Full Name and the position you are currently working on or the position you are applying for.</p>
                </div>
              </div>
              <div class="fields-section-content --file-section">
                 <div class="fields">
                  <div class="full-field --full-field">
                    <input id="profile-pic" type="file" @change="onprofilechange">
                    <label for="profile-pic" :class="ispicturepresent">
                      <div class="file-field">
                        <div class="label-vertical">
                          <div class="label-container">
                            <p v-if="hashcode">Look for Preview</p>
                            <p v-else>Upload image</p>
                          </div>
                        </div>
                      </div>
                    </label>
                  </div>
                </div>
              </div>
           </div>
           <div class="fields-section">
              <div class="fields-section-title">
                 <p>Core Info</p>
              </div>
              <div class="fields-section-hint">
                <div class="field-hint-inner">
                  <p>Basic information just includes your Full Name and the position you are currently working on or the position you are applying for.</p>
                </div>
              </div>
              <div class="fields-section-content --textarea-section">
                 <div class="fields">
                  <div class="full-field --full-field achievement-textarea">
                    <label>Career Objective</label>
                    <textarea placeholder="Enter Career Objective" v-model="objective" />
                  </div>
                </div>
              </div>
              <div class="fields-section-content --textarea-section">
                 <div class="fields">
                  <div class="full-field --full-field achievement-textarea">
                    <label>Core Skills</label>
                    <textarea placeholder="Skill Name 1 - Skill Name 2 - Skill Name 3 - Skill Name 4 - Skill Name 5 - Skill Name 6 - Skill Name 7 - Skill Name 8" v-model="core_skills" />
                  </div>
                </div>
              </div>
           </div>
           <div class="fields-section">
              <div class="fields-section-title">
                 <p>Rate your skills</p>
              </div>
              <div class="fields-section-hint">
                <div class="field-hint-inner">
                 <p>Basic information just includes your Full Name and the position you are currently working on or the position you are applying for.</p>
               </div>
              </div>
              <div class="skill-score-check">
                <div class="skill-score-check-inner">
                  <input type="checkbox" id="skill-check" v-model="skillpercent">
                  <label for="skill-check"></label>
                  <p>View percentage</p>
                </div>
              </div>
              <div class="fields-section-content">
                 <div class="special-field-wrapper field" v-for="(skill, count) in skillscore" :key="count">
                  <div class="special-field-card">
                    <div class="special-icon">
                       <i class="fas fa-sun"></i>
                    </div>
                    <div class="special-field">
                       <label> Skill {{ count + 1 }}</label>
                       <input placeholder="Enter skill name" type="text" v-model="skill.name" />
                     </div>
                     <div class="slider-box">
                       <input type="range" min="1" max="100" value="50" class="slider" v-model="skill.score" @input="calcwidth(count)">
                    </div>
                  </div>
                 </div>
              </div>
           </div>
           <div class="fields-section">
              <div class="fields-section-title">
                 <p>Career Timeline</p>
              </div>
              <div class="fields-section-hint">
                <div class="field-hint-inner">
                 <p> List your areas of experience (e.g., web analytics, content creation, social media management, etc.) or map out your previous roles and companies you’ve worked for – whichever you think works best for your situation.</p>
                 <ul>
                   <li>Your professional experience section should include all relevant work experience starting with your current or most recent position, if applicable.</li>
                   <li>Consider which experiences are most relevant to the next step you want to take in your career.</li>
                   <li>List your professional experience in reverse order.</li>
                 </ul>
               </div>
              </div>
              <div class="fields-section-content">
                 <div class="achievement-field-wrapper field">
                  <div v-for="(step, count) in timeline" :key="count" class="career-step">
                      <div class="section-sub-title">
                        <p>Enter details</p>
                        <div class="cancel-career-step" @click="deletestep(count)">
                          <i class="fas fa-times"></i>
                        </div>
                      </div>
                      <div class="fields">
                        <div class="field">
                          <label>Company name</label>
                          <input placeholder="Enter company name" type="text" v-model="step.organisation_name">
                        </div>
                        <div class="field">
                          <label>Position</label>
                          <input placeholder="Enter your position" type="text" v-model="step.position">
                        </div>
                      </div>
                      <div class="fields">
                        <div class="field">
                          <label>Job From</label>
                          <input placeholder="Enter job duration" type="text" v-model="step.from">
                        </div>
                        <div class="field">
                          <label>Job To</label>
                          <input placeholder="Enter job duration" type="text" v-model="step.to">
                        </div>
                      </div>
                      <div class="fields">
                        <div class="full-field --full-field achievement-textarea" v-for="(item, subcount) in step.achievements" :key="subcount">
                          <label>Achievement {{ (subcount + 1) }}</label>
                          <textarea placeholder="Enter your achievement here" v-model="item.data" />
                          <div class="achievement-options">
                            <div class="delete-achievement" @click="deleteachievement(count, subcount)">
                              <i class="fas fa-trash-alt"></i>
                              <div class="delete-achievement-p">
                                <div class="delete-achievement-p-inner">
                                  <p>Delete</p>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="add-achievement-button">
                        <div class="add-achievement-button-inner">
                          <p @click="addachievement(count)" title="Remove achievement"><i class="fas fa-plus-circle"></i> Add achievement</p>
                        </div>
                      </div>
                    </div>
                    <div class="add-company-step">
                      <div class="add-company-step-inner">
                        <p @click="addstep"><i class="fas fa-plus-circle"></i> Add career step</p>
                      </div>
                    </div>
                 </div>
              </div>
           </div>
           <div class="fields-section">
              <div class="fields-section-title">
                 <p>Education Information</p>
              </div>
              <div class="fields-section-hint">
                 <div class="field-hint-inner">
                  <p>Below are a few things to keep in mind when writing the Educational section in your resume.</p>
                  <ul>
                    <li>List your educational qualifications in reverse order</li>
                    <li>If you have a master’s and a bachelor’s degree, make sure to list the master’s degree first, followed by your bachelor’s degree.</li>
                  </ul>
                </div>
              </div>
              <div class="fields-section-content">
                 <div class="achievement-field-wrapper field">
                  <div v-for="(education, count) in educations" :key="count" class="career-step">
                      <div class="section-sub-title">
                        <p>Education {{ count + 1 }}</p>
                        <!--<div class="cancel-career-step" @click="deletestep(count)">
                          <i class="fas fa-times"></i>
                        </div>-->
                      </div>
                      <div class="fields">
                        <div class="field course-name-field">
                          <label>Course name</label>
                          <input placeholder="Enter course name" type="text" v-model="education.course_name">
                        </div>
                        <div class="field institution-field">
                          <label>Institution</label>
                          <input placeholder="Enter institution name" type="text" v-model="education.institute">
                        </div>
                      </div>
                      <div class="fields">
                        <div class="field duration-field">
                          <label>From</label>
                          <input placeholder="Enter duration" type="text" v-model="education.from">
                        </div>
                        <div class="field duration-field">
                          <label>To</label>
                          <input placeholder="Enter duration" type="text" v-model="education.to">
                        </div>
                        <div class="field marks-field">
                          <label>Marks</label>
                          <input placeholder="Enter marks" type="text" v-model="education.score">
                        </div>
                      </div>
                    </div>
                    <!--<div class="add-education-step">
                      <div class="add-education-step-inner">
                        <p @click="addeducation"><i class="fas fa-plus-circle"></i> Add education</p>
                      </div>
                    </div>-->
                 </div>
              </div>
           </div>
        </div>
    </div>
    <div id="template-preview">
      <div id="preview-inner">
          <PrimaryResume :hashcode="hashcode" :name="fullname" :position="position" :location="location" :emailid="emailid" :phone="phone" :profile="profile" :timeline="timeline" :skillscore="skillscore" :skills="skills" :educations="educations" :summary="summary" :objective="objective" :core_skills="core_skills" :facebook="facebook" :linkedin="linkedin" :github="github" :youtube="youtube" :twitter="twitter" :reddit="reddit" :behance="behance" :skillpercent="skillpercent" :picture="hashcode" />
        </div>
    </div>
    <div id="download-button">
      <Loading v-if="downloading" />
      <div v-else id="download-button-inner" @click="downloadResume">
        <i class="fas fa-download"></i>
      </div>
    </div>
  </div>
</template>

<script>
import Nav from '@/components/Nav'
import PrimaryResume from '@/resumes/PrimaryResume'
import Loading from '@/components/common/Loading'
import axios from 'axios'
export default {
  name: 'Primary',
  metaInfo: {
    title: 'Primary Template - My first ever Resume',
    titleTemplate: 'MarkMyCV - %s',
    htmlAttrs: {
      lang: 'en',
      amp: true
    }
  },
  components: {
    Nav,
    PrimaryResume,
    Loading
  },
  data () {
    return {
      hashcode: '',
      fullname: '',
      position: '',
      location: '',
      emailid: '',
      phone: '',
      professional: '',
      summary: '',
      objective: '',
      core_skills: '',
      profile: '',
      index: 0,
      professionalskills: '',
      timeline: [],
      skillscore: [
        { name: '', score: '50%' }, { name: '', score: '50%' }, { name: '', score: '50%' }, { name: '', score: '50%' }, { name: '', score: '50%' }, { name: '', score: '50' }
      ],
      skills: [],
      educations: [],
      facebook: '',
      linkedin: '',
      youtube: '',
      twitter: '',
      reddit: '',
      github: '',
      behance: '',
      skillpercent: false,
      datastring: '',
      savedboolean: false,
      ispicturepresent: false,
      background_status: '',
      overlay_class: '',
      login_username: '',
      downloading: false
    }
  },
  watch: {
    $data: function () { this.$data.savedboolean = true }
  },
  created () {
    let data = this.$data
    let access = 'Bearer ' + window.localStorage.getItem('access')
    axios({
      method: 'post',
      url: 'http://localhost:8000/api/get-profile',
      headers: {
        Authorization: access
      },
      data: { }
    }).then(function (response) {
      let bkup = JSON.parse(response.data.data)
      data.hashcode = bkup.hashcode
      data.fullname = bkup.fullname
      data.position = bkup.position
      data.location = bkup.location
      data.emailid = bkup.email_id
      data.phone = bkup.contact_no
      data.facebook = bkup.facebook
      data.twitter = bkup.twitter
      data.reddit = bkup.reddit
      data.linkedin = bkup.linkedin
      data.github = bkup.github
      data.youtube = bkup.youtube
      data.summary = bkup.summary
      data.objective = bkup.objective
      data.core_skills = bkup.core_skills
      data.skills = bkup.skills
      data.timeline = bkup.career_steps
      data.educations = bkup.educations
      data.image_upload_url = data.image_upload_url === '' ? 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQiIH_DHJMDLyBp2gUKTMyFA0jlPPF_Zya98x7B3hwJUy-2nKwn' : bkup.image_upload_url
    }).catch(function (error) {
      console.log(error)
    }).finally(function () { })
  },
  methods: {
    addachievement: function (count) { return this.timeline[count].achievements.push({ id: 0, index: 0, achievement: '' }) },
    addstep: function () { return this.timeline.push({ company: '', position: '', interval: '', achievements: [{ id: '0', achievement: '' }] }) },
    addeducation: function () { return this.educations.push({ course: '', college: '', duration: '', marks: '' }) },
    addskill: function () { return this.skills.push({ name: '', content: '' }) },
    addskillscore: function () { return this.skillscore.push({ name: '', content: '' }) },
    deleteeducation: function (count) { this.$data.educations.splice(count, 1) },
    deleteachievement: function (count, subcount) { this.$data.timeline[count].achievements.splice(subcount, 1) },
    deletestep: function (count) { this.$data.timeline.splice(count, 1) },
    deleteskill: function (count) { this.$data.skills.splice(count, 1) },
    calcwidth: function (count) {
      console.log('width: ' + this.$data.skillscore[count].score + '%;')
      this.$data.skillscore[count].style = 'width: ' + this.$data.skillscore[count].score + '%;'
    },
    savedoc: function () { localStorage.setItem('primary_template_data', JSON.stringify(this.$data)) },
    onprofilechange: function (e) {
      const url = 'http://localhost:8000/api/upload-image'
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
    closeHome (value) {
      let data = this.$data
      data.background_status = value
      if (value === 'opened') {
        data.overlay_class = 'opening'
        setTimeout(function () { data.overlay_class = 'opened' }, 10)
      } else {
        data.overlay_class = 'opening'
        setTimeout(function () { data.overlay_class = '' }, 500)
      }
    },
    downloadResume () {
      let data = this.$data
      let temp = {}
      temp.hashcode = data.hashcode
      temp.fullname = data.fullname
      temp.position = data.position
      temp.location = data.location
      temp.emailid = data.emailid
      temp.phone = data.phone
      temp.facebook = data.facebook
      temp.twitter = data.twitter
      temp.reddit = data.reddit
      temp.linkedin = data.linkedin
      temp.github = data.github
      temp.youtube = data.youtube
      temp.summary = data.summary
      temp.objective = data.objective
      temp.core_skills = data.core_skills
      temp.skillscore = data.skillscore
      temp.skills = data.skills
      temp.timeline = data.timeline
      temp.educations = data.educations
      data.downloading = true
      let access = 'Bearer ' + window.localStorage.getItem('access')
      axios({
        method: 'post',
        url: 'http://localhost:8000/api/download-primary-resume',
        // responseType: 'blob',
        headers: {
          Authorization: access
        },
        data: {
          'data': temp
        }
      }).then(function (response) {
        console.log(response.data.hashcode)
        const url = 'https://doc.markmycv.com/' + response.data.hashcode + '.pdf'
        const link = document.createElement('a')
        link.target = '_blank'
        link.href = url
        link.setAttribute('download', 'resume.pdf')
        document.body.appendChild(link)
        link.click()
        data.downloading = false
      }).catch(function (error) {
        console.log(error)
      }).finally(function () { })
    }
  }
}
</script>

<style lang="scss">
#templates-background{position: fixed;top: 0;left: 0;width: 100vw;height: 100vh;z-index: -1;background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('../images/home-bk.jpg');background-size: cover;background-position: center;transform: scale(1.1);filter: blur(2px);transition: 500ms left;
  &.opened{transform: scale(1.1);left: 20px;}
}
#template-editor{position: fixed;top: 120px;left: 4%;width: 46%;height: calc(100vh - 140px);background-color: rgba(255,255,255,0.1);border-radius: 5px;overflow-y: auto;}
#resume-editor{box-shadow: -2px 2px 5px 0 rgba(0,0,0,0.25);overflow-y: auto;
    #resume-editor-banner{
      #resume-editor-banner-inner{height: 324px;width: 100%;display: table;background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('../images/banner-editor.jpg');background-size: cover;background-position: center;box-shadow: inset 0 0 15px 0 rgba(0,0,0,0.15);}
      #resume-editor-banner-vertical{display: table-cell;vertical-align: middle;padding: 0 15px;text-align: center;
        p{text-shadow: -2px 2px 5px rgba(0,0,0,0.15);
          &.title{font-size: 38px;font-weight: bold;color: #eee;}
          &.content{font-size: 14px;font-weight: bold;color: #eee;}
        }
        hr{border: none;height: 4px;width: 50px;background-color: #eee;margin: 10px auto;border-radius: 2px;box-shadow: -2px 2px 5px 0px rgba(0,0,0,0.15);}
      }
    }
    #resume-editor-title{padding: 14px 16px 10px 16px;
      p{font-size: 14px;font-weight: bold;}
    }
    .skill-score-check{padding: 4px 15px;margin-top: 5px;
      &:after{clear: both;display: block;content: "";}
      .skill-score-check-inner{float: right;
        input{display: none;
          &:checked + label{background-color: #2ECC71;border: 1px solid #2ECC71;
            &:hover{background-color: #27AE60;border: 1px solid #27AE60;}
          }
        }
        label{background-color: #dddddd;float: left;width: 15px;height: 15px;margin-top: 0px;margin-right: 5px;padding: 0;border-radius: 5px;transition: 120ms;cursor: pointer;border: 1px solid #cccccc;box-sizing: border-box;margin-top: 1px;margin-bottom: 1px;
          &:hover{background-color: #cccccc;}
        }
        p{float: left;font-size: 11px;font-weight: bold;color: #fff;}
        &:after{clear: both;display: block;content: "";}
      }
    }
    .education-course{background-color: #fff;padding: 8px;box-shadow: -2px 2px 5px 0 rgba(0,0,0,0.15);border-radius: 5px;margin-top: 15px;
      .skill-name{width: 20%;}
      .skill-description{width: 80%;}
      .skill-name, .skill-description{float: left;padding: 0 8px 10px 8px;box-sizing: border-box;}
      input{width: 100% !important;}
      &:after{clear: both;display: block;content: ""}
      &:first-of-type{margin-top: 0px;}
    }
    .fields-section{padding: 12px 12px 4px 12px;
      &-title{padding: 0 8px;
        p{font-size: 12px;font-weight: bold;color: #fff;}
      }
      &-hint{padding: 8px 15px;
        .field-hint-inner{padding: 10px 10px;background-color: rgba(0,0,0,0.2);border-radius: 4px;color: #fff;}
        ul{margin-left: 22px;margin-top: 3px;
          li{font-size: 10.8px;font-weight: bold;margin-top: 3px;list-style-type: disc;}
        }
        p{font-size: 11px;font-weight: bold;}
      }
      .fields-section-content{
        label{color: #fff;}
        &.--textarea-section{padding: 0 10px;border-radius: 5px;margin-bottom: 15px;margin-top: 10px;
          .fields{background-color: rgba(0, 0, 0, 0.2);border-radius: 5px;box-shadow: -2px 2px 5px 0 rgba(0,0,0,0.15);padding: 5px;
          label{color: #fff;}
            textarea{border-radius: 5px 5px 5px 5px;border-bottom: 1px solid #eee;line-height: 16px;}
          }
        }
        &.--file-section{
          label{color: #fff;}
          .file-field{width: 100%;height: 100%;display: table;border: 3px dashed #ddd;box-sizing: border-box;}
          label{display: table !important;padding: 10px;box-sizing: border-box;color: #fff;cursor: pointer;transition: 120ms;
            .label-vertical{display: table-cell;vertical-align: middle;
              .label-container{text-align: center;color: #777;}
            }
            &:hover{background-color: #f6f6f6;}
          }
          input{display: none;}
          label{display: block;width: 30%;height: 160px;background-color: #eee;margin: 0 auto;
            &.true{background-color: #2ECC71;}
          }
        }
        .special-field-wrapper{width: 33.33%;float: left;box-sizing: border-box;}
        .section-sub-title{padding: 8px 10px 2px 10px;line-height: 16px;
          p{float: left;font-weight: bold;font-size: 13px;color: #fff;}
          .cancel-career-step{float: right;cursor: pointer;color: #fff;}
          &:after{clear: both;display: block;content: "";}
        }
        &:after{clear: both;display: block;content: "";}
      }
      .button-add-more{text-align: center;margin-bottom: 15px;
        .button-add-middle{
          .button-inner{background-color: #fff;margin: 0 auto;display: table;box-shadow: -2px 2px 5px 0 rgba(0,0,0,0.15);padding: 5px 10px;border-radius: 5px;cursor: pointer;
            .button-in{display: table-cell;vertical-align: middle;}
            p{font-size: 12px;font-weight: bold;float: left;}
            i{float: left;margin-right: 4px;}
          }
        }
      }
      &-content{padding: 5px 0px;
        .field{
          label{font-size: 11px;font-weight: bold;padding-left: 2px;padding-bottom: 2px;margin-top: 8px;
          }
          &:first-of-type{
            label{margin-top: 0;}
          }
          &:first-of-type{
            label{margin-top: 0;}
          }
          input{width: 60%;background-color: rgba(255,255,255,0.7);height: 32px;padding: 0 8px;box-sizing: border-box;font-size: 11px;font-weight: bold;border-radius: 5px;}
          label, input{display: block;}
        }
        .special-field-wrapper{width: 60%;padding: 8px;
          .special-field-card{background-color: rgba(0,0,0,0.2);box-shadow: -2px 2px 5px 0 rgba(0,0,0,0.15);padding: 10px 8px 12px 8px;border-radius: 4px;
            .slider-box{margin-top: 74px;margin-bottom: 12px;padding: 0 10px;}
            .slider{-webkit-appearance: none;width: 100%;height: 6px;background: #d3d3d3;outline: none;opacity: 1;transition: opacity .2s;padding: 0;margin-top: 10px;border: none;box-shadow: inset 0px 0px 2px 0 rgba(0,0,0,0.2);
              &:hover {opacity: 1;}
              &::-webkit-slider-thumb{-webkit-appearance: none;appearance: none;width: 18px;height: 18px;background: #333;cursor: pointer;border-radius: 50%;border: 4px solid #2ECC71;background: #fff;box-shadow: -2px 2px 5px 0 rgba(0,0,0,0.15);}
              &::-moz-range-thumb{width: 25px;height: 25px;background: #333;cursor: pointer;border-radius: 50%;}
            &:after{clear: both;display: block;content: "";}
          }
          .special-icon.social-icon{background-color: #fff;border-radius: 4px;}
          &:after{clear: both;display: block;content: "";}
          .special-icon{float: left;margin-right: 8px;margin-left: 4px;width: 50px;text-align: center;
            i{font-size: 48px;line-height: 52px;color: #fff;
              &.fa-github-square{color: #333333;}
              &.fa-facebook-square{color: #3b5998;}
              &.fa-twitter-square{color: #1da1f2;}
              &.fa-linkedin{color: #0077b5;}
              &.fa-linkedin{color: #0077b5;}
              &.fa-reddit-square{color: #ff4500;}
              &.fa-behance-square{color: #1769ff;}
              &.fa-youtube{color: #ff0000;font-size: 42px;}
              &.fa-map-marker-alt{font-size: 40px;}
              &.fa-envelope{font-size: 40px;}
              &.fa-phone{font-size: 38px;}
              &.fa-crosshairs{font-size: 38px;}
              &.fa-user{font-size: 38px;}
            }
          }
          .special-field{float: left;width: calc(100% - 62px);
            label{margin: 0;color: #fff;}
            input{width: 100%;}
          }
          &:after{clear: both;display: block;content: "";}
        }
      }
    }
    .achievement-field-wrapper{padding: 8px;
      .achievement-options{width: 100%;background: rgba(255, 255, 255, 0.7);border-radius: 0px 0px 5px 5px;margin-top: -7px;padding: 5px 10px;box-sizing: border-box;border-top: none;
      .delete-achievement{float: right;background-color: #E74C3C;padding: 2px 6px;border-radius: 4px;cursor: pointer;transition: 180ms;
        .delete-achievement-p{width: 0px;overflow-x: hidden;transition: 500ms;}
        .delete-achievement-p-inner{width: 44px;margin-left: 4px;}
        &:hover{
          .delete-achievement-p{width: 44px;}
        }
        p{font-size: 12px;font-weight: bold;float: left;line-height: 22px;color: #eee;}
        i{color: #eee;line-height: 22px;float: left;font-size: 12px;}
        &:hover{background-color: #C0392B;}
      }
      &:after{clear: both;display: block;content: "";}
    }
      .career-step{background-color: rgba(0, 0, 0, 0.2);padding: 10px 8px 12px 8px;border-radius: 5px;box-shadow: -2px 2px 5px 0 rgba(0,0,0,0.15);margin-top: 15px;
        .fields{
          &:after{clear: both;display: block;content: "";}
          .field{width: 50%;float: left;padding: 8px;box-sizing: border-box;
            label{font-size: 12px;font-weight: bold;padding-left: 2px;padding-bottom: 2px;margin-top: 8px;color: #fff;
            }
            input{width: 100%;background-color: rgba(255,255,255,0.7);height: 32px;padding: 0 8px;box-sizing: border-box;font-size: 12px;font-weight: bold;border-radius: 5px;}
            label, input{display: block;}
            &.course-name-field{width: 50%;}
            &.institution-field{width: 50%;}
            &.duration-field{width: 33.33%;}
            &.marks-field{width: 33.33%;}
            &:after{clear: both;display: block;content: "";}
          }
          .full-field{width: 100%;float: none;padding: 0 8px;box-sizing: border-box;margin: 8px 0;}
        }
        .add-achievement-button{padding-top: 5px;
          .add-achievement-button-inner{text-align: center;
            p{font-weight: bold;font-size: 12px;background-color: #2ECC71;color: #fff;display: inline-block;padding: 4px 10px;border-radius: 5px;cursor: pointer;transition: 180ms;
              i{vertical-align: baseline;}
              &:hover{background-color: #27AE60;}
            }
          }
        }
        &:first-of-type{margin-top: 0px;}
      }
    }
    label{font-size: 12px;font-weight: bold;padding-left: 2px;padding-bottom: 2px;margin-top: 8px;}
    .achievement-textarea{padding: 0 8px;}
    textarea{width: 100%;background-color: rgba(255,255,255,0.7);height: 32px;padding: 8px;box-sizing: border-box;font-size: 12px;font-weight: bold;border-radius: 5px 5px 0 0;height: 100px;resize: none;border-bottom: none;line-height: 16px;}
    .add-company-step, .add-education-step{background-color: #fff;text-align: center;margin-top: 15px;border-radius: 5px;box-shadow: -2px 2px 5px 0 rgba(0,0,0,0.15);padding: 5px 0;font-weight: bold;font-size: 13px;cursor: pointer;
      p{font-size: 12px;}
    }
  }
}
#template-preview{position: fixed;width: 46%;right: 4%;top: 120px;}
#download-button{position: fixed;bottom: 15px;right: 15px;background-color: #2ECC71;cursor: pointer;height: 48px;width: 48px;display: table;border-radius: 50%;transition: 150ms;
  #download-button-inner{display: table-cell;vertical-align: middle;text-align: center;
    i{font-size: 22px;color: #fff;}
  }
  .sk-circle{margin: 11px auto;width: 26px;height: 26px;}
  &:hover{background-color: #27AE60;}
}
  @media(min-width: 1200px) and (max-width: 1400px) {
    #editor-area{width: calc(100vw - 600px);}
    #preview-area{width: 600px;}
    //.page{transform: scale(0.5) translate(-25%, -50%);}
    #resume-editor .fields-section .fields-section-content .special-field-wrapper{width: 50%;}
  }
  @media (max-width: 1200px) {
    #resume-editor .fields-section .fields-section-content .special-field-wrapper{width: 50%;}
  }
  @media print {
    #dashboard-nav, #editor-area, #save-document{display: none;}
    #editor-content{padding-top: 0px;}
  }
</style>
