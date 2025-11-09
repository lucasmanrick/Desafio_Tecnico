import { View,ImageBackground, TouchableOpacity, Text } from "react-native";
import {style} from './styles';
import { LinearGradient } from "expo-linear-gradient";
import { useAuth } from "../../hooks/useAuth";


export default function ModalCripto(props:any) {
    const {isAuthenticated} = useAuth();

    return(
        <LinearGradient style={style.modal} key={props.id}
        colors={['#000000ff','#000a70ff']} // cores do gradiente
        start={{ x: 1, y: 0.5 }}
        end={{ x: 1, y: 0 }}
        >
            <ImageBackground source={{uri: props.image}} style={style.modalImage} resizeMode="contain">
                <Text style={style.title}>{props.name}</Text>
                <View style={style.infoView}>
                    <Text style={style.symbol}>{props.symbol.toUpperCase()}</Text>
                    {isAuthenticated? 
                    (<View style={style.buttonContainer}>
                        <TouchableOpacity style={style.buttonStyle}><Text style={style.text}>Favoritar Moeda</Text></TouchableOpacity>
                        <TouchableOpacity style={style.buttonStyle}><Text style={style.text}>Incluir no Portfolio</Text></TouchableOpacity>
                    </View>):''
                }
                </View>
            </ImageBackground>
        </LinearGradient>
    )
}