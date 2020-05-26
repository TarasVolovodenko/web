<template>
<div class="issue_description">
    <span class="header">{{data_for_issue.title}}</span>
    <div class="sub-header">
        <span class="tag">{{data_for_issue.pollution_category}}</span>
        <span class="date">{{data_for_issue.date}}</span>
    </div>
    <div class="rating">
        <span>Pollution rating: {{data_for_issue.pollution_rating}}</span>
    </div>

    <p class="description">
        {{data_for_issue.description}}
        s </p>
</div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'issue_description',
    data() {
        return {
            data_for_issue: []
        }
    },
    methods: {},
    mounted() {
        axios
            .get("http://localhost:5000/api/issue/3").then(response => {
                this.data_for_issue = response.data;
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
    line-height: $header-fline-hight;
    line-height: 54px;
}

.tag {
    margin-right: 2vw;
}

.sub-header {
    color: $accent-fcolor;
    font-size: $fsize;
    // line-height:$fline-hight;
    margin-top: 3px;
}

.rating {
    color: $accent-fcolor;
    font-size: $accent-fsize;
    // line-height:$accent-fline-hight;
    margin: 1vw 0;
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

    .sub-header,
    .description {
        font-size:calc(#{$fsize} - 5px);
        margin-top: 0;
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

    .sub-header,
    .description {
        font-size:calc(#{$fsize} - 6px);
        margin-top: 0;
    }

    .rating {
        font-size:calc(#{$accent-fsize} - 9px);
        margin: 0.5vw 0;
    }
}

@media only screen and (max-width: 910px) {
    .header {
        font-size:calc(#{$header-fsize} - 23px);
        line-height: 36px;
    }

    .sub-header,
    .description {
        font-size:calc(#{$fsize} - 8px);
    }

    .rating {
        font-size:calc(#{$accent-fsize} - 13px);

    }
}
</style>
