<template>
<li class="issue-card col50 flex-sp-between">
    <div class="issue-image">
        <img :src="issue.imgurl" alt="img">
    </div>
    <div class="issue-container">
        <div class="issue-header">
            <p>{{issue.title}}</p>
        </div>
        <div class="issue-tag-date">
            <div class="issue-tag">
                <p>{{issue.type}}</p>
            </div>
            <div class="issue-date">
                <p>{{issue.date}}</p>
            </div>
        </div>
        <div class="issue-rating">
            <p>Pollution rating: {{issue.rating}}</p>
        </div>
        <div class="issue-decsribtion">
            <p>{{issue.text}}</p>
        </div>
        <a :href="issue.link">
            <div class="issue-link">
                <div class="issue-link-text">
                    <p>Read more</p>
                </div>
                <div class="issue-link-icon">
                    <img src="logo/arrowRight.svg" alt=">">
                </div>
            </div>
        </a>
    </div>
</li>
</template>

<script>
export default {
    name: 'issueDesc',
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

.issue-image{
    width: 200px;
    height: 200px;
    margin-right: 25px;
}

.issue-container{
    width: 360px;
    height: 200px;
}

.issue-header > p{
    font-weight: 500;
    font-size: 26px;
    line-height: 32px;
    
    color: #D3D3D3;
}

.issue-decsribtion > p, .issue-link-text > p{
    font-style: normal;
    font-weight: normal;
    font-size: 20px;
    line-height: 24px;

    color: #D3D3D3;
}

.issue-link{
    display: flex;
    flex-direction: row;
}

.issue-link-icon{
    margin-left: 6px;
}
</style>