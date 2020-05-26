<template>
<div class="comment_card row ">
    <div class="comment-photo">
        <img id="image0" :src="comment_data.author.avatar">
    </div>
    <div class="comment_text col-sm-9">
        <p class="comment-header">{{comment_data.author.name}}</p>
        <p class="comment-sub">Pollution rating: {{comment_data.pollution_rating}}</p>
        <p :class="{'comment-text-hide': this.isActive,'comment-text-show': !this.isActive}" id="comment-text">{{comment_data.text}}</p>

        <a href="javascript:void();" class="more-btn" :class="{'more-btn': !this.isActive,'more-btn-hide': !this.isActive}" v-on:click="expandCollapse()">See more</a>
    </div>
</div>
</template>

<script>
export default {
    name: 'comment_card',
    data() {
        return {
            isActive: true,
            comment_data: []
        }
    },
    methods: {
        expandCollapse() {
            this.isActive = !this.isActive;
        }
    },
    props: [
        'comment'
    ],
    beforeMount() {
        this.comment_data = this.comment;
    }
}
</script>

<style lang="scss" scoped>
.comment_card {
    background: transparent;
    margin: 27px 0;
}

.comment-header,
.more-btn {
    color: $accent-fcolor;
    font-size: $accent-fsize;
    // line-height: $accent-fline-hight;
}

.more-btn {
    padding: 9px 0px;
}

.comment-sub,
#comment-text {
    color: $fcolor;
    font-size: $fsize;
    line-height: $fline-hight;
}

.comment-sub {
    padding: 9px 0px;
}

.comment-photo {
    padding-left: 21px;
}

.comment-text-hide {
    display: block;
    display: -webkit-box;
    height: 3*$fline-hight;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
}

.comment-text-show {
    display: block;
}

.more-btn-hide {
    display: none;
}

@media only screen and (max-width: 1330px) {

    .comment-header,
    .more-btn {
        font-size: calc(#{$accent-fsize} - 7px);
    }

    .comment-sub,
    #comment-text {
        font-size:calc(#{$fsize} - 5px);
    }

}

@media only screen and (max-width: 1150px) {
    .comment_card {
        margin: 1vw 0;
    }

    .comment-header,
    .more-btn {
        font-size: calc(#{$accent-fsize} - 9px);
    }

    .more-btn {
        padding: 9px 0px;
    }

    .comment-sub,
    #comment-text {
        font-size:calc(#{$fsize} - 7px);
    }

    .comment-sub {
        padding: 0.4vw 0px;
    }

    .comment-photo {
        padding-left: 1vw;
    }

    img {
        height: 85px;
        width: auto;
    }

}

@media only screen and (max-width: 910px) {

    .comment-header,
    .more-btn {
        font-size: calc(#{$accent-fsize} - 13px);
    }

    .more-btn {
        padding: 7px 0px;
    }

    .comment-sub,
    #comment-text {
        font-size:calc(#{$fsize} - 9px);
    }

    img {
        height: 75px;
        width: auto;
    }

}
</style>
