import { StyleSheet } from "react-native";

export const style = StyleSheet.create({
    container:{
        padding:0,
        flex:1,
        backgroundColor: 'black'
    },

    header:{
        width: '100%',
        height: '10%',
        // backgroundColor:'#ffffffff',
        // boxShadow: '0px 20px 20px rgba(0, 0, 0, 0.25)',
        display:'flex',
        flexDirection:'row',
        justifyContent:'space-between',
        alignItems:'center',
        padding:10
    },
    textLogin:{
        color: 'white',
        fontSize:18,
        fontWeight:'bold'
    },

     welcomeMessage:{
        width: '100%',
        height: 300,
        display:'flex',
        justifyContent:'center',
        alignItems:'center',

     },

    title:{
        textAlign:'center',
        fontSize: 30,
        fontWeight: '900',
        color: 'white'
    },

    mainContent:{
        display:'flex',
        flexDirection:'column',
        alignItems:'center',
        padding:10,
        gap:50,
        width: '100%',
        flexGrow:1
    },

    quitButton:{
        width:60,
        height:60,
        borderRadius:'50%',
        borderColor:'white',
        borderWidth:2,
        backgroundColor:'#ef0000ff',
        opacity: 1,
        position:'absolute',
        bottom: 100,
        right: 50,
        display:'flex',
        justifyContent:'center',
        alignItems:'center'
    }
})