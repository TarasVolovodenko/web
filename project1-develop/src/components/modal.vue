<template>
  <transition name="fade" appear>
    <div class="overlay" v-if="showModal">
      <div class="modal">
          <div class="modal-content">
            <div class="cross-block">
            <a class="cross" @click="closeModal()"></a>
            </div>
            <div class="modal-header">
              <slot name="header"></slot>
            </div>
            <div class="modal-body">
              <slot name="body"></slot>
            </div>
            <div class="modal-footer">
              <slot name="footer"></slot>
            </div>
        </div>
      </div>
    </div>
  </transition>
</template>
<script>
export default {
  name: 'app-modal',
  props: {
    showModal: Boolean
  },
  methods: {
    closeModal () {
      this.$emit('clicked')
    }
  }
}
</script>
<style>
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 98;
  background-color: rgba(0, 0, 0, 0.5);
}
.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 20px;
  background: #FFFFFF;
  overflow-x: auto;
  display: flex;
  flex-direction: column;
}
.modal-header, .modal-body, .modal-footer {
  display: flex;
  justify-content: center;
  min-height: 50%;
}
.modal-footer {
  align-content: flex-end;
}
.cross-block {
  width: 100%;
  height: 20px;
}
.cross {
  display: block;
  float: right;
  width: 20px;
  height: 20px;
  background-image: url(../resources/cross-icon.svg);
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  cursor: pointer;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
