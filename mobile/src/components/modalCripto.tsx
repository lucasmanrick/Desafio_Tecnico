import { View,ImageBackground, TouchableOpacity, Text } from "react-native";
import {style} from './styles';


export default function ModalCripto(props:any) {
    return(
        <View style={[style.modal]}>
            <ImageBackground source={{uri: props.image}} style={style.modalImage}>
                <View style={style.buttonContainer}>
                    <TouchableOpacity><Text>Favoritar Moeda</Text></TouchableOpacity>
                    <TouchableOpacity><Text>Incluir no Portfolio</Text></TouchableOpacity>
                </View>
            </ImageBackground>
        </View>
    )
}