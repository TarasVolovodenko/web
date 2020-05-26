<template>
  <div class="DonateContent">
    <div id="donate-info">
      <h2>Why you should donate?</h2>
      <p>1.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tortor erat, placerat ac sollicitudin nec, vulputate et felis. Nulla sed augue quis nisl rhoncus varius a non sem. Praesent pulvinar elit ut risus gravida tincidunt. Donec egestas diam vitae diam vestibulum feugiat. In ut orci non ante finibus fermentum. Donec lobortis est non velit ultricies pretium. In sed sagittis ante, eu accumsan nisi.</p>
      <p>2.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tortor erat, placerat ac sollicitudin nec, vulputate et felis. Nulla sed augue quis nisl rhoncus varius a non sem. Praesent pulvinar elit ut risus gravida tincidunt. Donec egestas diam vitae diam vestibulum feugiat.</p>
    </div>
    <form>
      <h2>Choose amount</h2>
      <div class="money">
        <div class="money-btns">
          <CustomButton name="10$" :class="{highlight:selected_btn == 0}" @click="other = false, selected_btn = 0"/>
          <CustomButton name="20$" :class="{highlight:selected_btn == 1}" @click="other = false, selected_btn = 1"/>
          <CustomButton name="50$" :class="{highlight:selected_btn == 2}" @click="other = false, selected_btn = 2"/>
          <CustomButton name="Other" :class="{highlight:selected_btn == 3}" @click="other = true, selected_btn = 3"/>
        </div>
        <TextField v-if="other" class="donate-field" id="other"/>
      </div>
      <h2>Billing information</h2>
      <div class="billing">
        <div class="column">
          <h3>First name</h3>
          <TextField class="donate-field" value = {data_for_donate.name} id="first-name"/>
        </div>
        <div class="column">
          <h3>Last name</h3>
          <TextField class="donate-field" value = {data_for_donate.surname} id="last-name"/>
        </div>
        <div class="column">
          <h3>Email</h3>
          <TextField class="donate-field" value = {data_for_donate.email} id="email"/>
        </div>
        <div class="column">
          <h3>City</h3>
          <TextField class="donate-field" value = {data_for_donate.city} id="city"/>
        </div>
      </div>
      <h2 id="payment-title">Payment information</h2>
      <div class="payment-contribution">
        <div class="payment">
          <div class="card-info">
            <div class="column">
              <h3>Card number</h3>
              <TextField class="donate-field" id="card-number"/>
            </div>
            <div class="column">
              <h3>MM/DD</h3>
              <TextField class="donate-field" id="expiration-date"/>
            </div>
            <div class="column">
              <h3>CVV</h3>
              <TextField class="donate-field" id="CVV"/>
            </div>
          </div>
          <div class="owner-column">
            <h3>Owner's name</h3>
            <TextField class="donate-field" id="owner-name"/>
          </div>
        </div>
        <div class="contribution">
          <h3>Recurring Contribution</h3>
          <p>Give monthly to ensure our work can continuing.</p>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
          <div class="contribution-mark">
            <label class="checkmark-container"> Make this a Recurring Contribution
              <input type="checkbox" id="recurring-contribution" checked="checked">
              <span class="checkmark"></span>
            </label>
          </div>
        </div>
      </div>
      <CustomButton :name="donate_btn" id="donate-btn"/>
    </form>
    <div class="sponsor-info">
      <h2>ECOMAP sponsors</h2>
      <p>Ecomap is about community</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      <p>And it wouldn’t be possible without our sponsors. Feel free to email us for additional info.</p>
      <div class="icon-line">
        <span class="email-icon icon"></span>
        <h3>mail_sponsor@mail.com</h3>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CustomButton from '@/components/buttontd.vue'
import TextField from '@/components/textfield.vue'
export default {
  name: 'DonateContent',
  components: {
    CustomButton,
    TextField
  },
  data () {
    return {
      selected_btn: 0,
      other: false,
      donate_btn: 'Donate now',
      data_for_donate: []
    }
  },
  methods: {
  },
  mounted(){
    axios.post("http://localhost8080/api/donate").then(response =>{this.data_for_donate = response.data})
    .catch(error => {console.log(error)})
  }
}
</script>

<style lang="scss">
.DonateContent h2 {
  padding-top: 50px;
}
#donate-info p {
  padding: 40px 75px 0px;
  font-size: 24px;
}
.DonateContent form {
  margin: 0px 50px;
}
.highlight {
  background-color: $white;
}
 .highlight span {
  color: $dark-color;
 }
.money {
  display: flex;
  flex-direction: column;
  margin-top: 50px;
}
.money-btns {
  display: flex;
  justify-content: space-between;
}
.donate-field {
  height: 60px;
  box-sizing: border-box;
  border-color: $white;
  background: transparent;
  margin: 0;
  color: $white;
}
#other {
  align-self: flex-end;
  margin-top: 20px;
  width: 300px;
}
.billing {
  display: flex;
  justify-content: space-between;
  margin-top: 50px;
}
.billing .donate-field {
  width: 250px;
}
.billing h3 {
  padding: 8px;
}
#payment-title {
  text-align: left;
}
.payment-contribution {
  display: flex;
  margin-top: 50px
}
.payment {
  width: 60%;
  padding-right: 100px;
}
.contribution {
  width: 40%;
}
.contribution h3 {
  margin-bottom: 20px;
}
.contribution .contribution-mark {
  margin-top: 20px;
  display: inline-block;
}
.card-info {
  display: flex;
  justify-content: space-between;
}
#card-number, #owner-name {
  width: 400px;
}
#expiration-date, #CVV {
  width: 120px;
}
.owner-column {
  margin-top: 20px;
}
#donate-btn {
  margin: 50px 0;
}
.sponsor-info p, .sponsor-info h2, .sponsor-info .icon-line {
  margin: 0 50px;
}
.sponsor-info h2 {
  text-align: left;
  margin-bottom: 25px;
}
.sponsor-info .icon-line {
  margin-top: 25px;
  margin-bottom: 100px;
}
.sponsor-info .icon {
  margin: 0 25px 0 0;
}

.checkmark-container {
  display: block;
  position: relative;
  padding-left: 35px;
  margin-bottom: 12px;
  cursor: pointer;
  font-size: 22px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.checkmark-container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}
.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 25px;
  width: 25px;
  background-color: $white;
  transition: 0.2s;
}
.checkmark-container:hover input ~ .checkmark {
  background-color: $fcolor;
}
.checkmark-container input:checked ~ .checkmark {
  background-color: $white;
}
.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}
.checkmark-container input:checked ~ .checkmark:after {
  display: block;
}
.checkmark-container .checkmark:after {
  left: 7px;
  top: 2px;
  width: 7px;
  height: 15px;
  border: solid $dark-color;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}
</style>
