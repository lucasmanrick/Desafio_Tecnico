import { StyleSheet } from "react-native";

export const style = StyleSheet.create({
    container:{
        padding:0,
        marginTop: 50,
        width: '100%',
        height: '100%'
    },

    header:{
        width: '100%',
        height: '20%',
        // backgroundColor:'#ffffffff',
        // boxShadow: '0px 20px 20px rgba(0, 0, 0, 0.25)',
        display:'flex',
        justifyContent:'center',
        alignItems:'center'
    },

    title:{
        fontSize: 40,
        fontWeight: '900',
        color: 'white'
    },

    mainContent:{
        display:'flex',
        justifyContent:'center',
        alignItems:'center',
        width: '100%',
        height: '70%'
    },

    text:{
        fontSize: 20,
        fontWeight: 'bold',
        color: 'white'
    },

    inputStyle:{
        width: '70%',
        height: 50,
        borderWidth: 1,
        borderRadius: 10,
        backgroundColor:'white'
    },

    buttonContainer:{
        width: '100%',
        height: '20%',
        display:'flex',
        flexDirection:'column',
        justifyContent:'space-evenly',
        alignItems:'center',
        marginTop: 5
    },

    button: {
        width: '40%',
        height: 50,
        backgroundColor: 'white',
        display:'flex',
        justifyContent:'center',
        alignItems:'center',
        borderRadius: 10
    },

    buttonText: {
        fontSize: 20,
        fontWeight: 'bold',
        color: 'black'
    }
})