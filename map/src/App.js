// import './App.css';
// import React, { Component } from 'react';
// // import { Key } from './key' // 引入 API key
// import GoogleMapReact from 'google-map-react';

// const AnyReactComponent = ({ text }) => <div>{text}</div>;

// // Map
// class SimpleMap extends Component {
//   static Key = 'AIzaSyC_Za7RqKvUuEg2Nln0EcpUVN3k2fZtDuE'
//   static defaultProps = {
//     center: {
//       lat: 25.0416463,
//       lng: 121.5527911
//     },
//     zoom: 11
//   };

//   render() {
//     return (
//       // Important! Always set the container height explicitly
//       <div style={{ height: '100vh', width: '100%' }}>
//         <GoogleMapReact
          
//           bootstrapURLKeys={{ key: this.Key }} //API key
//           defaultCenter={this.props.center} // default map vision
//           defaultZoom={this.props.zoom} //預設縮放視角
//         >
//           <AnyReactComponent
//             lat={25.0652883}
//             lng={121.5772416}
//             text="Cathy bank south Neihu"
//           />
//         </GoogleMapReact>
//       </div>
//     );
//   }
// }

// //App
// function App() {
//   return (
//     <div className="App">
//       <SimpleMap />
//     </div>
//   );
// }

// export default App;

import React from 'react';
import {Map, InfoWindow, Marker, GoogleApiWrapper} from 'google-map-react';

export class GMap extends React.Component {
  state = {
    showingInfoWindow: false,
    activeMarker: {},
    selectedPlace: {},
  };

  onMarkerClick = (props, marker, e) =>
    this.setState({
      selectedPlace: props,
      activeMarker: marker,
      showingInfoWindow: true
    });

  onMapClicked = (props) => {
    if (this.state.showingInfoWindow) {
      this.setState({
        showingInfoWindow: false,
        activeMarker: null
      })
    }
  };

  render() {
    return (
      <Map google={this.props.google}
           initialCenter={{
             lat: 39.9060115,
             lng: 116.3956187
           }}
           zoom={16.75}
           onClick={this.onMapClicked}>
        <Marker onClick={this.onMarkerClick}
                name={'descripton'}
                position={{lat: 39.9055688, lng: 116.39749}}/>

        <InfoWindow
          marker={this.state.activeMarker}
          visible={this.state.showingInfoWindow}>
          <div>
            <h3>{this.state.selectedPlace.name}</h3>
          </div>
        </InfoWindow>
      </Map>
    )
  }
}

export default GoogleApiWrapper({
  apiKey: ('AIzaSyC_Za7RqKvUuEg2Nln0EcpUVN3k2fZtDuE')
})(GMap)