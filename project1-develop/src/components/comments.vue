<template>
<div class="comments">
    <span class="header">Comments</span>
    <b-container fluid v-if="this.visible">
        <div class="row ">
            <div class="row">
                <div class="add_comment col-sm-6">
                    <span>Add comment</span>
                    <div v-if="this.registered">
                        <div class="rate">
                            <input type="text" value="" onchange="this.setAttribute('value', this.value)" class="col-sm-6 rate_input" />
                            <span class="placeholder">Pollution rating(1-5)</span>
                        </div>
                        <div class="comment">
                            <input type="text" value="" onchange="this.setAttribute('value', this.value)" class="col-sm-12 comment_input" />
                            <span class="placeholder">Comment</span>
                        </div>
                        <custom_button :name="bname" class="cbtn"></custom_button>
                    </div>
                    <div v-else d-block>
                        <p class="not-reg">Please log in or register to add comments.</p>
                    </div>
                </div>
                <div class="my-1 col-6" :key="index" v-for="(item, index) in paginatedItems.slice(0,3)">
                    <comment_card :comment="item"></comment_card>
                </div>
            </div>
        </div>
        <div class="collapse_btn d-flex justify-content-center">
            <a href="javascript:void();" v-on:click="toggleItems">Show all<i class="arrow fas fa-caret-down" /></a>
        </div>
    </b-container>
    <b-container fluid v-else>
        <b-row>
            <div class="add_comment col-sm-6 d-flex flex-column">
                <span>Add comment</span>
                <div v-if="this.registered">
                    <div class="rate">
                        <input type="text" value="" onchange="this.setAttribute('value', this.value)" class="col-sm-6 rate_input" />
                        <span class="placeholder">Pollution rating(1-5)</span>
                    </div>
                    <div class="comment">
                        <input type="text" value="" onchange="this.setAttribute('value', this.value)" class="col-sm-12 comment_input" />
                        <span class="placeholder">Comment</span>
                    </div>
                    <custom_button :name="bname" class="cbtn"></custom_button>
                </div>
                <div v-else>
                    <p class="not-reg">Please log in or register to add comments.</p>
                </div>
            </div>
            <div class="my-1 col-6" :key="index" v-for="(item, index) in paginatedItems">
                <comment_card :comment="item"></comment_card>
            </div>
        </b-row>
        <b-row>
            <b-col md="12" class="my-1">
                <b-pagination @change="onPageChanged" :total-rows="totalRows" :per-page="perPage" v-model="currentPage" class="my-0 pagination" align="center" />
            </b-col>
        </b-row>
        <div class="collapse_btn d-flex justify-content-center">
            <a href="javascript:void();" v-on:click="toggleItems">Hide all <i class="fas fa-caret-up arrow" /></a>
        </div>
    </b-container>
</div>
</template>

<script>
import custom_button from '@/components/button'
import comment_card from '@/components/comment_card.vue'


export default {
    name: 'comments',
    components: {
        custom_button,
        comment_card
    },
    props: ['cdata'],

    computed: {
        pageCount() {
            let l = this.totalRows,
                s = this.perPage;
            return Math.floor(1 + l / s);
        },
        setData() {

        }
    },
    data: function () {
        return {
            items: [],
            paginatedItems: [],
            perPage: 9,
            totalRows: 10,
            currentPage: 1,
            visible: true,
            registered: false,
            bname: 'Publish'
        };
    },
    mounted() {
        this.paginate(this.perPage, 0);
    },
    methods: {
        paginate(page_size, page_number) {
            let itemsToParse = this.items;
            this.paginatedItems = itemsToParse.slice(
                page_number * page_size,
                (page_number + 1) * page_size
            );
        },

        onPageChanged(page) {
            this.paginate(this.perPage, page - 1);
        },
        toggleItems() {
            this.visible = !this.visible;
        }
    },
    beforeMount() {
        this.items = this.cdata;
        this.paginatedItems = this.cdata;
        this.totalRows = this.cdata.length;
    }
};
</script>

<style lang="scss" scoped>
.header {
    color: $accent-fcolor;
    font-size: $header-fsize;
    line-height: $header-fline-hight;
    padding-bottom: 2px;
}

.add_comment {
    color: $accent-fcolor;
    font-size: $accent-fsize;
    line-height: $accent-fline-hight;
    margin: 32px 0;
}

.rate,
.comment {
    position: relative;
    padding-top: 1.5vw;
}

.comment {
    padding-right: 50px;
}

.placeholder {
    font-size: $fsize;
    line-height: $fline-hight;
    position: absolute;
    bottom: 15px;
    left: 0;
}

.rate_input,
.comment_input {
    background-color: transparent;
    color: $fcolor;
    border: none;
    border-bottom: 1px solid $fcolor;
    padding-bottom: 6px;
}

.rate_input:focus,
.comment_input:focus {
    outline: none;
}

.rate_input:focus~span,
.comment_input:focus~span {
    display: none;
}

.rate_input:not([value=""]):not(:focus)~span,
.comment_input:not([value=""]):not(:focus)~span {
    display: none;
}

.cbtn {
    margin: 32px 0;
}

.collapse_btn {
    text-align: center;
    padding: 20px;
}

.arrow {
    margin: 3px 10px;
    color: #FFFFFF;
}

.not-reg {
    font-size: $fsize;
    line-height: $fline-hight;
    color: $accent-fcolor;
    margin-top: 7px;
}

// .my-1:nth-of-type(odd) {
//     float: left;
//     width:50%;

// }
.my-1:nth-of-type(even) {
    padding-left: 50px;
}

// .my-1:last-child
// {
//   clear:both;
// }

@media only screen and (max-width: 1150px) {
    .my-1:nth-of-type(even) {
        padding-left: 2.5vw;
    }

    .header {
        font-size: calc(#{$header-fsize} - 15px);
        padding-bottom: 2px;
    }

    .add_comment {
        font-size: calc(#{$accent-fsize} - 7px);
        margin: 1vw 0;
    }

    .not-reg {
        font-size: calc(#{$fsize} - 5px);
    }

    .rate_input,
    .comment_input {
        padding-bottom: 4px;
    }

    .comment {
        padding-right: 2.5vw;
    }

    .placeholder {
        font-size: calc(#{$fsize} - 5px);
        bottom: 10px;
    }

}

@media only screen and (max-width: 910px) {

    .header {
        font-size: calc(#{$header-fsize} - 23px);
        padding-bottom: 2px;
    }

    .add_comment {
        font-size: calc(#{$accent-fsize} - 9px);
        margin: 1vw 0;
    }

    .not-reg {
        font-size: calc(#{$fsize} - 7px);
    }

    .placeholder {
        font-size: calc(#{$fsize} - 7px);
        bottom: 8px;
    }

}
</style>
