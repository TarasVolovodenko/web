<template>
  <div class="navbar">
    <div class="logo">
      <a href="." class="site-logo icon"></a>
      <a href="." class="site-name">ECOMAP</a>
    </div>
    <div class="links">
      <router-link to="/">Home</router-link>
      <router-link to="/issues">Issues</router-link>
      <router-link to="/fixed">Fixed</router-link>
      <router-link to="/events">Events</router-link>
      <router-link to="/donate">Donate</router-link>
      <router-link to="/contacts">Contacts</router-link>
    </div>
    <div class="buttons">
      <div class="dropdown">
        <a class="dropbtn" @click="dropdown_active = !dropdown_active">{{lang}}<div id="lang-arrow" :class="dropdown_active ? 'lang-arrow-up' : 'lang-arrow-down'"/></a>
        <div class="dropdown-content" v-bind:class="{hidden: dropdown_active == false}">
          <a @click="lang='EN'; dropdown_active = !dropdown_active">EN</a>
          <a @click="lang='UA'; dropdown_active = !dropdown_active">UA</a>
          <a @click="lang='RU'; dropdown_active = !dropdown_active">RU</a>
        </div>
      </div>
      <a class="nav-btn user-btn" @click="onLoginChildClick(); openLoginModal()" :href="user_logged_in ? '.' : '#'"/>
      <div class="search-container">
        <form action="">
          <input type="text" placeholder="Type your text here" name="search" :class="{search_hidden: display_search_bar == false}">
          <a class="nav-btn search-btn" @click="display_search_bar = !display_search_bar"/>
        </form>
      </div>
    </div>
    <app-modal v-if="loginModal" :showModal=loginModal @clicked="onLoginChildClick()" id="login-modal">
      <div slot="header" class="login-header">
        <h2>User login</h2>
      </div>
      <form class="login-form" slot="body">
        <TextField placeholder="E-mail" class="login-field" id="email-login-field"/>
        <TextField placeholder="Password" class="login-field" id="password-login-field"/>
        <CustomButton @click="onLoginChildClick();" name="Log in" class="submit-btn" />
        <CustomButton @click="onLoginChildClick();" name="Sign in" class="submit-btn" />
      </form>
      <div slot="footer">
      </div>
    </app-modal>
  </div>
</template>

<script>
import AppModal from '@/components/modal.vue'
import TextField from '@/components/textfield.vue'
import CustomButton from '@/components/buttontd.vue'
export default {
  name: 'NavBar',
  components: {
    AppModal,
    TextField,
    CustomButton
  },
  data () {
    return {
      display_search_bar: false,
      loginModal: false,
      user_logged_in: false,
      lang: 'EN',
      dropdown_active: false
    }
  },
  methods: {
    openLoginModal () {
      if (!this.user_logged_in) {
        this.loginModal = true
      }
    },
    onLoginChildClick () {
      this.loginModal = false
    }
  }
}
</script>
<style lang="scss">
.navbar {
  display: flex;
  position: relative;
  margin: 40px 70px;
}
.links {
  display: flex;
  justify-content: space-evenly;
  width: 40%;
}
.links a, .dropdown a {
  height: 30px;
  font-size: 20px;
  text-decoration: none;
  padding: 5px;
  color: $font-color;
  text-decoration: none;
  box-sizing: border-box;
  cursor: pointer;
}
.links .router-link-exact-active, .links a:hover {
  border-bottom-style: solid;
}
.logo {
  display: flex;
  width: 30%;
}
.logo .icon {
  margin: 0px;
}
.site-name {
  height: 30px;
  font-size: rem(30);
  color: $white;
  padding-left: 10px;
  text-decoration: none;
}
.buttons {
  display:flex;
  align-items: center;
  justify-content: flex-end;
  width: 30%;
}
.nav-btn {
  height: 16px;
  width: 16px;
  background-size: cover;
  margin: 7px;
  cursor: pointer;
}
.search-btn {
  background-image: url("../resources/search-icon.svg");
}
.user-btn {
  background-image: url("../resources/user.svg");
}
.search-container {
  height: 30px
}
.search-container form {
  display: flex;
}
.search_hidden {
  display: none;
}
.search-container input {
  width: 250px;
  font-family: 'Montserrat', sans-serif;
  background-color: transparent;
  font-size: 20px;
  color: $font-color;
  outline-style: none;
  padding-left: 10px;
  padding-right: 10px;
  border-style: hidden hidden solid hidden;
  border-color: $font-color;
}

.submit-btn {
  border-color: $dark-color;
  margin-top: 15px;
}
.submit-btn span {
  color: $dark-color;
}
.login-form {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}
.login-field {
  width: 400px;
}
.login-header {
  color: $dark-color;
}
#login-modal .modal-body {
  padding-left: 100px;
  padding-right: 100px;
}
.dropdown {
  height: 30px;
}
.dropdown-content a {
  border-style: solid;
  border-width: 1px;
}
.dropdown-content, .dropdown {
  display: flex;
  flex-direction: column;
}
.dropdown-content a:hover {
  background-color: $fcolor;
  border-color: $font-color;
  color: black;
}
.hidden {
  display: none;
}
#lang-arrow {
  height: 10px;
  width: 12px;
  margin-left: 8px;
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}
.lang-arrow-down {
  background-image: url("../resources/lang-arrow-down.svg");
}
.lang-arrow-up {
  background-image: url("../resources/lang-arrow-up.svg");
}
.dropbtn {
  display: flex;
  align-items: center;
}
</style>
