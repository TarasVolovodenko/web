<template>
<div>
    <Header />
    <main>
        <div id="title" class="flex-center">
        <div id="" class="">
                <h2>Issues in the world</h2>
            </div>
        </div>

        <section id="map-module" class="">
            <div id="filters-container" class="" >
                <ul id="filters">
                    <li id="filter-trash" class=""><p>Trash</p></li>
                    <li id="filter-air" class="highlighted"><p>Air pollution</p></li>
                    <li id="filter-water" class=""><p>Water pollution</p></li>
                    <li id="filter-clear" class=""><p>Clear filters</p></li>
                </ul>
            </div>
            
            <div id="map-container" class="flex-center">
                <div id="map-window" class="">

                    <!--Тут будет Вова-->
                    <!--{{ message }}-->
                    <div id="map-box"></div>
                    
                </div>
                <div id="bla-bla-map" class="">
                    <div id="article-header" class="map-header">
                        <p>This map is bla bla</p>
                    </div>
                    <article id="" class="">
                        <p>Lorem ipsum dolor si amet bla bla ok islddsldl alscf v, dxv. 
                            Lorem ipsum dolor si amet bla bla ok islddsldl alscf v, dxv. 
                            Lorem ipsum dolor si amet bla bla ok islddsldl alscf v, dxv.</p>
                    </article>
                    <div id="map-btns-container" class="">
                        <!-- <div id="btn-area" class="map-header map-btn">
                            <p>Issues in this area</p>
                        </div> -->
                        <custom_button id="btn-area" name="Issues in this area"></custom_button>
                        <custom_button id="btn-area" name="Issues nearby"></custom_button>
                        <!-- <div id="btn-nearby" class="map-header map-btn flex-center">
                            <p>Issues nearby</p>
                        </div> -->
                    </div>
                </div>
            </div>                            

        </section>

        <section id="list-module" class="">
            <ul id="issue-list" class="flex-sp-between">
                <issueDesc v-for="issue in Object.entries(issues)" v-bind:issue="issue[1]" v-bind:key="issue.id"></issueDesc>
            </ul>
        </section>

    </main>
    <Footer />
</div>
</template>

<script>
import Vue from 'vue'
import mapboxgl from 'mapbox-gl'
import Header from '@/layout/header'
import Footer from '@/layout/footer'
import markerPopup from '@/components/issue_map_popup'
import issueDesc from '@/components/issue_map_description'
import custom_button from '@/components/button'

// Vue.loadScript("https://api.mapbox.com/mapbox-gl-js/v1.9.1/mapbox-gl.js")

export default {
    name: 'issuesMap',
    components: {
        Header,
        Footer,
        markerPopup,
        issueDesc,
        custom_button
    },
    data() {
        return {
            issues: [],
            markers: [],
            map: null,
            filter: '',
            area_button: "Issues in this area"
        }
    },
    mounted() {
        mapboxgl.accessToken = "pk.eyJ1IjoidGhlLWJyYWluaWVzdCIsImEiOiJjazI5ZGZ3eTUwN3g0M25ycDkyeWNmZGVyIn0.UANPt67xKag8limygO6I-g";
        this.map = new mapboxgl.Map({
            container: "map-box",
            // style: "mapbox://styles/mapbox/streets-v11",
            style: "mapbox://styles/the-brainiest/ck9he8o6z0y091iqwllxzpvqh",
            center: [30.092674, 51.387285],
            zoom: 8
        });
        this.map.on('moveend', data => {this.updateIssues();});
        document.getElementById('btn-area').onclick = this.updateIssues;
        document.getElementById('btn-nearby').onclick = this.updateIssues;
        document.getElementById('filter-trash').onclick = () => {this.filter = '1'; this.updateIssues(); };
        document.getElementById('filter-air').onclick = () => {this.filter = '3'; this.updateIssues(); };
        document.getElementById('filter-water').onclick = () => {this.filter = '2'; this.updateIssues(); };
        document.getElementById('filter-clear').onclick = () => {this.filter = ''; this.updateIssues(); };
        this.updateIssues();
    },
    methods: {
        updateIssues() {
            console.log('Updating');
            this.getIssues(this.map.getCenter().toArray()).then(issues => {
                var ids = '';
                Object.entries(issues).forEach(issue => {
                    ids += ',';
                    ids += issue[0];
                })
                this.getIssueDetails(ids.substring(1)).then(issuesDet => {
                    this.issues = issuesDet;
                    this.markers.forEach(marker => {
                        marker.remove();
                    });
                    this.markers = [];
                    Object.entries(issuesDet).forEach(issueDet => {
                        issueDet = issueDet[1];
                        this.markers.push(this.createMarker(issueDet).setLngLat(
                            new mapboxgl.LngLat(issueDet.lat, issueDet.lon))
                            .addTo(this.map)
                        );
                    });
                });
            });
        },
        getIssues() {
            var p1 = this.map.getBounds().getSouthWest();
            var p2 = this.map.getBounds().getNorthEast();
            var bbox = '('+p1.lat+','+p1.lng+'),('+p2.lat+','+p2.lng+')'
            return fetch('http://localhost:5000/api/getIssuesShort?bbox=' + bbox
                + '&count=300'+'&pollution_type='+this.filter)
                .then(response => response.json());
        },
        getIssueDetails(id) {
            return fetch('http://localhost:5000/api/getIssues?ids='+id).then(response => response.json());
        },
        createMarker(issue) {
            var markerDiv = document.createElement('div');
            markerDiv.className = 'map-marker';
            var MarkerPopup = Vue.extend(markerPopup);
            var popupEl = new MarkerPopup({propsData: {issue: issue}}).$mount();
            // popupEl.setAttibute('issue', issue);
            popupEl['issue'] = issue;
            // var popup = new mapboxgl.Popup().setHTML('<h5>' + issue.name + '</h5>')
            var popup = new mapboxgl.Popup().setDOMContent(popupEl.$el);
            return new mapboxgl.Marker(markerDiv).setPopup(popup);
        }
    }
}

</script>

<style>

@import "https://fonts.googleapis.com/css?family=Montserrat&display=swap";
@import "https://api.mapbox.com/mapbox-gl-js/v1.9.1/mapbox-gl.css";

.map-marker {
    width: 7px;
    height: 7px;
    cursor: pointer;
    background-color: red;
    border-radius: 50%;
    border-color: black;
    border-width: 1px;
    border-style: solid;
}

#map-container{
    padding: 40px 0;
}

.map-header{
    font-weight: 500;
    font-size: 26px;
    line-height: 32px;
    text-align: center;
}

#article-header{
    text-align: left;
    line-height: 24px;
}

article{
    font-weight: normal;
    font-size: 20px;
    line-height: 24px;
    margin: 15px 0;
}

.map-btn{
    border: 1px solid #F2F2F2;
    margin: 5px 0;
    height: 60px;
    line-height: 60px;
}

#map-box {
    width: 975px;
    height: 627px;
    margin: 0 40px 0 0;
}

#issue-container map-popup{
    display: flex;
    align-items: center;
    justify-content: center;
    width: 420px;
    height: 250px;
    color: #201F30;
}

#issue-tag-date {
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: normal;
    font-size: 20px;
    line-height: 24px;
}

#issue-rating {
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: normal;
    font-size: 20px;
    line-height: 24px;
}

/* List module*/

#list-module{
    padding: 75px 0;
}

#issue-card{
    display: flex;
    width: 50%;
}

#issue-list > li{
    margin: 26px 62px;
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

#title{
    padding: 10px;
}

h2{
    font-weight: 500;
    font-size: 52px;
    line-height: 63px;
    color: #D3D3D3;
}

#filters{
    padding: 5px;
    display: flex;
    flex-direction: row;
}

#filters > li{
    padding: 0 20px;
}

#filters > li > p{
    font-weight: 500;
    font-size: 26px;
    line-height: 32px;

    opacity: 0.5;
}

body{
    margin: 0 auto;
    font-family: Montserrat, sans-serif;
    font-size: 20px;
    max-width: 1440px;
    box-sizing: border-box;
    background: #1B1919;
}

ul {
    display: block;
    margin: 0;
    padding: 0;
    list-style: none;
}

a{
    text-decoration: none;
    color: #F2F2F2;
}

p{
    margin: 0;
    color: #F2F2F2;
}

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

.align-center{
    align-items: center;
}

.hidden{
    display: none;
}

</style>