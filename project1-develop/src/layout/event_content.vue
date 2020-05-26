<template>
<div class="content">
    <div class="row justify-content-center no-gutters">
        <carousel class="carousel col-6 mr-auto "></carousel>
        <div class="description col">
            <event_description></event_description>
            <custom_button :name="bname" class="bm"></custom_button>
        </div>
    </div>
    <div class="comments">
        <comments v-if="mnt" :cdata="comments_data"></comments>
    </div>
</div>
</template>

<script>
import carousel from '@/components/carousel'
import event_description from '@/components/event_description'
import custom_button from '@/components/button'
import comments from '@/components/comments'
import comment_card from '@/components/comment_card.vue'
import axios from 'axios'

export default {
    name: 'Content',
    components: {
        carousel,
        event_description,
        custom_button,
        comments,
        comment_card
    },

    data() {
        return {
            bname: 'Participate',
            comments_data: [],
            mnt: false
        }
    },
    mounted() {
        axios
            .get("http://localhost:5000/api/event/1/comments").then(response => {
                this.comments_data = response.data;
                this.mnt = true;
            })
            .catch(error => {
                console.log(error)
            })
    }

}
</script>

<style lang="scss" scoped>
.content {
    padding: 70px;
}

.description {
    margin-left: 51px;

}

.bm {
    margin-top: 2vw;
}

.comments {
    margin-top: 2vw;
}

@media only screen and (max-width: 1250px) {

    .content {
        padding: 4vw;
    }

    .description {
        margin-left: 2.5vw;
    }
}
</style>
