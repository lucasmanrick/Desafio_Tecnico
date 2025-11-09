import { StyleSheet } from "react-native";

export const style = StyleSheet.create({

    modal:{
        width: '100%',
        height: 300,
        display:'flex',
        justifyContent:'center',
        alignItems:'center',
        backgroundColor: '#2d2d2dff',
    },

    modalImage:{
        width: '100%',
        height: '100%',
        display:'flex',
        flexDirection:'column',
        justifyContent:'space-between'
    },

    title:{
        fontSize: 20,
        fontWeight: 'bold',
        color: 'white'
    },

    text:{
        fontSize: 20,
        fontWeight: 'bold',
        color: 'white'
    },

    infoView:{
        width: '100%',
        height: '40%',
        display:'flex',
        flexDirection:'row',
        justifyContent:'space-between',
        alignItems:'center',
        backgroundColor: '#0000006b'
    },

    symbol:{
        color: '#ffffffff',
        fontSize:30,
        fontWeight: '900'
    },

    buttonContainer:{
        display:'flex',
        flexDirection:'column',
        justifyContent:'center',
        width: '50%',
        gap:5,
        height: '100%'
    },

    buttonStyle: {
        width:'100%',
        height:'40%',
        display:'flex',
        justifyContent:'center',
        alignItems:'center',
        borderRadius:10,
        color: 'white'
    },
})