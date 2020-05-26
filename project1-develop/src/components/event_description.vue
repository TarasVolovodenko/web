<template>
<div class="event_description">
    <span class="header">{{data_for_event.title}}</span>
    <div class="sub-header1 d-flex justify-content-between">
        <span class="tag">{{data_for_event.pollution_category}}</span>
        <span class="date">{{data_for_event.date}}</span>
        <span class="participate"> People involved: {{data_for_event.participants}}</span>
    </div>
    <div class="rating">
        <span>Pollution rating: {{data_for_event.pollution_rating}}</span>
    </div>
    <div class="sub-header2">
        <span>Why is it necessary?</span>
    </div>

    <p class="description">
        {{data_for_event.text}}
    </p>
</div>
</template>

<script>
import axios from 'axios'

export default {

    name: 'event_description',
    data() {
        return {
            data_for_event: []
        }
    },
    methods: {},
    mounted() {
        axios
            .get("http://localhost:5000/api/event/1").then(response => {
                this.data_for_event = response.data;
            })
            .catch(error => {
                console.log(error)
            })
    }

}
</script>

<style lang="scss" scoped>
.header {
    color: $accent-fcolor;
    font-size: $header-fsize;
    line-height: 54px;
}

.sub-header1 {
    color: $accent-fcolor;
    font-size: $fsize;
    // line-height:$fline-hight;
    margin-top: 3px;
    width: 70%;
}

.sub-header2 {
    color: $accent-fcolor;
    font-size: 40px;

    margin-bottom: 0.8vw;

    // line-height:$fline-hight;
}

.rating {
    color: $accent-fcolor;
    font-size: $accent-fsize;
    // line-height:$accent-fline-hight;
    margin: 0.8vw 0;
}

.description {
    color: $accent-fcolor;
    font-size: $fsize;
    // line-height:$fline-hight;
}

@media only screen and (max-width: 1330px) {
    .header {
        font-size:calc(#{$header-fsize} - 10px);
        line-height: 45px;
    }

    .sub-header1,
    .description {
        font-size:calc(#{$fsize} - 5px);
    }

    .sub-header2 {
        font-size: 35px;
    }

    .rating {
        font-size:calc(#{$accent-fsize} - 7px);
        margin: 0.5vw 0;
    }
}

@media only screen and (max-width: 1100px) {
    .header {
        font-size:calc(#{$header-fsize} - 15px);
        line-height: 42px;
    }

    .sub-header1,
    .description {
        font-size:calc(#{$fsize} - 6px);
        margin-top: 0;
    }

    .sub-header1 {
        width: 80%;
    }

    .rating {
        font-size:calc(#{$accent-fsize} - 9px);
        margin: 0.5vw 0;
    }

    .sub-header2 {
        font-size: 30px;
    }

}

@media only screen and (max-width: 910px) {
    .header {
        font-size:calc(#{$header-fsize} - 23px);
        line-height: 36px;
    }

    .sub-header1,
    .description {
        font-size:calc(#{$fsize} - 9px);
    }

    .rating {
        font-size:calc(#{$accent-fsize} - 13px);

    }

    .sub-header1 {
        width: 90%;
    }

    .sub-header2 {
        font-size: 27px;
    }

}
</style>
