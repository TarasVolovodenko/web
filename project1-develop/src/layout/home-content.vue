<template>
  <div class="HomeContent" id="home-content">
    <Slider :slider_title="slider_titles.first" :urls="urls.first" :image_urls="image_urls.first" :titles="titles.first" :descriptions="descriptions.first"/>
    <Slider class="slider2" :slider_title="slider_titles.second" :urls="urls.second" :image_urls="image_urls.second" :titles="titles.second" :descriptions="descriptions.second"/>
    <div class="problem">
      <div class="problem-text">
        <p class="problem-title">
          Do you know about one more problem?
        </p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. </p>
        <CustomButton @click="onContactChildClick(); openContactModal()" id="contact-button" name="Contact us"/>
      </div>
      <div class="problem-img"/>
    </div>
    <app-modal v-if="contactModal" :showModal=contactModal @clicked="onContactChildClick()" id="new-issue-modal">
      <div slot="header" class="new-issue-header">
        <h2>Tell about new issue</h2>
      </div>
      <form class="new-issue-form" slot="body">
        <TextField placeholder="Name" value = {data_for_issue.title} class="new-issue-field"/>
        <TextField placeholder="Category" value  = {data_for_issue.category} class="new-issue-field"/>
        <TextField placeholder="Pollution rating (in your opinion)" value = {data_for_issue.pollutionrating} class="new-issue-field"/>
        <TextField placeholder="Place" value = {data_for_issue.location} class="new-issue-field"/>
        <TextField placeholder="Description" value = {data_for_issue.descriptions} class="new-issue-field"/>
        <TextField placeholder="Link to photo" value = {data_for_issue.link} class="new-issue-field"/>
        <CustomButton @click="onContactChildClick(); openSubmitModal()" name="Submit" class="submit-btn" />
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
</template>

<script>
import axios from "axios"
import Slider from '@/components/slider.vue'
import CustomButton from '@/components/buttontd.vue'
import AppModal from '@/components/modal.vue'
import TextField from '@/components/textfield.vue'
export default {
  name: 'HomeContent',
  components: {
    Slider,
    CustomButton,
    AppModal,
    TextField

  },
  data () {
    return {
      slider_titles: {
        first: 'Fixed',
        second: 'New'
      },
      urls: {
        first: ['', '', '', '', ''],
        second: ['', '', '', '', '']
      },
      image_urls: {
        first: ['https://imaginion.files.wordpress.com/2011/08/surealistic-hdr-staw-chief-third-peak.jpg?w=1000', '', '', '', ''],
        second: ['https://www.dw.com/image/44067444_401.jpg', '', '', '', '']
      },
      titles: {
        first: ['Salish Sea', '', '', '', ''],
        second: ['Majorka beach', '', '', '', '']
      },
      descriptions: {
        first: ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.', '', '', '', ''],
        second: ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.', '', '', '', '']
      },
      contactModal: false,
      submitModal: false,
      data_for_issue: []
    }
  },
  methods: {
    openContactModal () {
      this.contactModal = true
    },
    openSubmitModal () {
      this.submitModal = true
    },
    onContactChildClick () {
      this.contactModal = false
    },
    onSubmitChildClick () {
      this.submitModal = false
    }
  },
  mounted(){
    axios
      .post("http://localhost8080/api/issue").then(response =>{
        this.data_for_issue = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style lang="scss">
.slider2 {
  background-color: $dark-color;
}
.problem {
  padding: 100px 0 100px 100px;
  display: flex;
}
.problem-title {
  font-size: 64px;
}
.problem-img {
  width: 650px;
  height: 450px;
  min-width: 650px;
  background-image: url("../resources/problem.jpg");
  background-size: cover;
  justify-self: flex-end;
}
.problem-text {
  padding: 30px 30px 30px 0;
}
#contact-button {
  margin: 30px 0 0 0;
}

.new-issue-form {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}
.new-issue-field {
  width: 400px;
}
.new-issue-header {
  color: $dark-color;
}
#new-issue-modal .modal-body {
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
</style>
