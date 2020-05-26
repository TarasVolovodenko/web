<template>
  <div class="contacts-content">
    <div class="title">
      <h2>Contacts</h2>
    </div>
    <div class="container">
      <div class="column-60">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        <h3>Want to join us?</h3>
        <p>Ecomap is our growing project. Together, we can begin to restore nature and improve the state of our planet. Fill in the form below to join us.</p>
        <CustomButton @click="openAdminModal()" :name="admin_btn" id="admin-btn" />
        <app-modal v-if="adminModal" :showModal=adminModal @clicked="onAdminChildClick()" id="admin-modal">
          <div slot="header" class="admin-header">
            <h2>Become admin</h2>
          </div>
          <form class="admin-form" slot="body">
            <TextField placeholder="Name" value = {data_for_admin.name} class="admin-field"/>
            <TextField placeholder="E-mail" value = {data_for_admin.email} class="admin-field"/>
            <TextField placeholder="Message" value = {data_for_admin.message} class="admin-field"/>
            <TextField placeholder="About" value = {data_for_admin.about} class="admin-field"/>
            <TextField placeholder="Additional info" value = {data_for_admin.additional_info} class="admin-field"/>
            <TextField placeholder="Link on resume / info" value = {data_for_admin.link} class="admin-field"/>
            <CustomButton @click="submit_admin(); onAdminChildClick(); openSubmitModal()" :name="submit_btn" class="submit-btn" />
          </form>
          <div slot="footer">
          </div>
        </app-modal>
        <app-modal v-if="submitModal" :showModal=submitModal @clicked="onSubmitChildClick()" class="submit-modal">
          <div slot="body">
            <h3>Thank you for your contribution</h3>
          </div>
          <div slot="footer">
            <a class="submit-icon" @click="onSubmitChildClick()"></a>
          </div>
        </app-modal>
      </div>
      <div class="column-40">
        <div class="icon-line">
            <span class="email-icon icon"></span>
            <h3>mail@mail.com</h3>
        </div>
        <div class="icon-line">
            <span class="location-icon icon"></span>
            <h3>UK st. Strada 31a, office 3</h3>
        </div>
        <div class="icon-line">
            <span class="phone-icon icon"></span>
            <h3>+2 28327 238 34 56</h3>
        </div>
      </div>
    </div>
    <div class="error">
      <p id="error1">Found an error?</p>
      <p id="error2" @click="openErrorModal()">write us</p>
    </div>
    <app-modal v-if="errorModal" :showModal=errorModal @clicked="onErrorChildClick()" id="error-modal">
          <div slot="header" class="error-header">
            <h2>Technical issue</h2>
          </div>
          <form class="error-form" slot="body">
            <div class="name">
              <TextField placeholder="First name" value = {data_for_tech.name} class="name-field"/>
              <TextField placeholder="Last name" value = {data_for_tech.surname} class="name-field"/>
            </div>
            <TextField placeholder="E-mail" value = {data_for_tech.email} class="error-field"/>
            <TextField placeholder="Message" value = {data_for_tech.message} class="error-field"/>
            <label class="media-file submit-btn btn">
              <input type="file"/>
                <span>Upload media</span>
            </label>
            <CustomButton @click="submit_tech(); onErrorChildClick()" name="Send message" class="submit-btn" />
          </form>
          <div slot="footer" class="error-contacts">
            <span>Contact information</span>
            <div class="icon-line">
              <span class="email-icon-black icon"></span>
              <span>mail@mail.com</span>
            </div>
            <div class="icon-line">
              <span class="location-icon-black icon"></span>
              <span>UK st. Strada 31a, office 3</span>
            </div>
          </div>
        </app-modal>
  </div>
</template>

<script>
import CustomButton from '@/components/buttontd.vue'
import AppModal from '@/components/modal.vue'
import TextField from '@/components/textfield.vue'
export default {
  name: 'ContactsContent',
  components: {
    CustomButton,
    AppModal,
    TextField
  },
  data () {
    return {
      admin_btn: 'Become admin',
      submit_btn: 'Submit',
      adminModal: false,
      submitModal: false,
      errorModal: false,
      data_for_admin: [],
      data_for_tech: []
    }
  },
  methods: {
    openAdminModal () {
      this.adminModal = true
    },
    openSubmitModal () {
      this.submitModal = true
    },
    openErrorModal () {
      this.errorModal = true
    },
    onAdminChildClick () {
      this.adminModal = false
    },
    onSubmitChildClick () {
      this.submitModal = false
    },
    onErrorChildClick () {
      this.errorModal = false
    },
    submit_admin(){
      axios.post("http:\\localhost8080\api\AdminRequest". then(response =>{
        this.data_for_admin = response.data
      }))
      .catch(error => console.log(error))
    },
    submit_tech(){
      axios.post("http:\\localhost8080\api\TechIssue". then(response =>{
        this.data_for_admin = response.data
      }))
      .catch(error => console.log(error))
    }
  }
}
</script>

<style lang="scss">
.title {
  display: flex;
  justify-content: center;
  height: 52px;
}
.container {
  display: flex;
}
.column-60 {
  width:60%;
  padding: 30px 75px;
}
.column-40 {
  width:40%;
  padding: 30px 75px 30px 0px;
}
.icon-line {
  display: flex;
  align-items: center;
  padding: 5px 0px;
}
.column-40 span {
  display: block;
}
.column-60 p, .column-60 h3 {
  padding-bottom: 30px;
}
.admin-form, .error-form {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}
.admin-field, .error-field {
  width: 400px;
  box-sizing: border-box;
}
.name-field {
  width: 180px;
  box-sizing: border-box;
}
.admin-header, .error-header {
  color: $dark-color;
}
.modal-body {
  padding-left: 100px;
  padding-right: 100px;
}
.submit-modal h3 {
  text-align: center;
  color: $dark-color;
  padding: 5px;
}
.submit-modal .modal-body {
  padding: 0 15%;
}
.submit-icon {
  display: block;
  width: 50px;
  height: 50px;
  margin-top: 20px;
  background-image: url(../resources/confirmation-icon.svg);
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  border-radius: 50%;
  transition: 0.5s;
  cursor: pointer;
}
.submit-icon:hover {
  background-color: $fcolor;
}
.error {
  margin-top: 20px;
  margin-bottom: 20px;
  font-size: 18px;
}
.error * {
  text-align: center;
}
#error2 {
  color: #3e5076;
  cursor: pointer;
  transition-property: color;
  transition: 0.5s;
}
#error2:hover {
  color: #4c6fb6;
}
.name {
  display: flex;
  width: 400px;
  justify-content: space-between;
}
input[type="file"] {
    display: none;
}
.media-file {
  display: flex;
  align-content: center;
  background-image: url("../resources/paper-clip.svg");
  background-repeat: no-repeat;
  background-size: 30px 30px;
  background-position: 10% 50%;
}
.error-contacts {
  display: flex;
  flex-direction: column;
  color: black;
  width: 300px;
}
.error-contacts>* {
  margin-top: 10px;
}
.email-icon-black {
  background-image: url("../resources/email-icon-black.svg");
}
.location-icon-black {
  background-image: url("../resources/location-icon-black.svg");
}
.error-contacts .icon {
  width: 20px;
  height: 20px;
  margin: 0 10px 0 0;
}
</style>
