<template>
<button type="button" class="btn btn-outline-light">
    <span>{{name}}</span>
</button>
</template>

<script>
export default {
    name: 'custom_button',
    data() {
        return {}
    },
    props: [
        'name'
    ],

    methods: {}
}
</script>

<style lang="scss">
.btn {
    border: 1px solid white;
    width: 300px;
    height: 60px;
    //$btn-border-radius-base:0!important;
}

.btn:hover span {
    color: $bcolor;
}

.btn:hover {
    background-color: $fcolor;
}

.btn span {
    color: $fcolor;
    font-size: $accent-fsize;
    // line-height: $accent-fline-hight;
    font-family: 'Montserrat', sans-serif;
}

@media only screen and (max-width: 1150px) {
    .btn span {
        font-size: calc(#{$accent-fsize} - 9px);
    }

    .btn {
        border: 1px solid white;
        width: 200px;
        height: 50px;
        //$btn-border-radius-base:0!important;
    }

}

@media only screen and (max-width: 910px) {
    .btn {
        border: 1px solid white;
        width: 200px;
        height: 50px;
        //$btn-border-radius-base:0!important;
    }

}
</style>
