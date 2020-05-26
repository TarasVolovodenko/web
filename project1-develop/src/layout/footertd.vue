<template>
<div class="Footer">
  <a href="https://twitter.com/" id="twitter" class="icon"></a>
  <a href="https://telegram.org/" id="telegram" class="icon"></a>
  <a href="https://www.instagram.com/" id="instagram" class="icon"></a>
</div>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style lang="scss">
.Footer {
  display: flex;
  justify-content: center;
  padding: 25px 0px;
  background: $dark-color;

  margin-top: auto;
}
#twitter {
    background-image: url(../resources/twitter.svg);
}

#telegram {
    background-image: url(../resources/telegram.svg);
}

#instagram {
    background-image: url(../resources/instagram.svg);
}

</style>
