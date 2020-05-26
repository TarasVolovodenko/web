<template>
<div class="popup-container map-popup">
    <div class="popup-header">
        <p>{{issue.title}}</p>
    </div>
    <div class="popup-tag-date">
        <div class="popup-tag">
            <p>{{issue.type}}</p>
        </div>
        <div class="popup-date">
            <p>{{issue.date}}</p>
        </div>
    </div>
    <div class="popup-rating">
        <p>Pollution rating: {{issue.rating}}</p>
    </div>
    <div class="popup-decsription">
        <p>{{issue.text}}</p>
    </div>
    <a :href="issue.link">
        <div class="popup-link">
            <div class="popup-link-text">
                <p>Read more</p>
            </div>
            <div class="popup-link-icon">
                <img src="logo/arrowRight.svg" alt=">">
            </div>
        </div>
    </a>
</div>
</template>

<script>
export default {
    name: 'markerPopup',
    data() {
        return {
            issue: {}
        }
    }
}
</script>

<style scoped>

.col33{
    width: 33%;
    margin: 0 15px;
}

.col50{
    width: 50%;
}

.col66{
    width: 66%;
}

.h100{
    height: 100%;
}

.flex-center{
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.flex-sp-between{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.flex-col-sp-between{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.map-popup > * > p{
    color: #201F30;
}

.map-popup > * > * > p{
    color: #201F30;
}

.map-popup > * > * > * > p{
    color: #201F30;
}

</style>