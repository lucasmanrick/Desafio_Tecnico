import { View, ImageBackground, TouchableOpacity, Text, Alert } from "react-native";
import { style } from './styles';
import { LinearGradient } from "expo-linear-gradient";
import { useAuth } from "../../hooks/useAuth";
import { RegisterRequest, AddFavoriteRequest, FavoriteCoin } from '../../types/'
import { api } from "../../api/axios";

export default function ModalCripto(props: any) {
    const { isAuthenticated , accessToken} = useAuth();


    const favoriteCoin = async (CoinId: string) => {

        const payload: AddFavoriteRequest = { coin_id: CoinId }

        try {
            const response = await api.post<FavoriteCoin>('/favorites/', payload, {
                headers:{
                    Authorization: `Bearer ${accessToken}`
                }
            })


            if (response.status === 201) {
                Alert.alert("Sucesso", "Moeda favoritada com sucesso!")
            }

        } catch (error) {
            console.log("erro ao tentar favoritar moeda: ", error)
            Alert.alert("Erro", "Nao foi possivel favoritar a moeda, tente novamente!")
        }
    }

    return (
        <LinearGradient style={style.modal} id={props.id} 
            colors={['#000000ff', '#000a70ff']} // cores do gradiente
            start={{ x: 1, y: 0.5 }}
            end={{ x: 1, y: 0 }}
        >
            <ImageBackground source={{ uri: props.image }} style={style.modalImage} resizeMode="contain">
                <Text style={style.title}>{props.name}</Text>
                <View style={style.infoView}>
                    <Text style={style.symbol}>{props.symbol.toUpperCase()}</Text>
                    {isAuthenticated && props.homepage === 'S' ?
                        (<View style={style.buttonContainer}>
                            <TouchableOpacity onPress={() => favoriteCoin(props.id)} style={style.buttonStyle}>
                                <Text style={style.text}>Favoritar Moeda</Text></TouchableOpacity>
                            <TouchableOpacity style={style.buttonStyle}><Text style={style.text}>Incluir no Portfolio</Text></TouchableOpacity>
                        </View>) : ''
                    }
                </View>
            </ImageBackground>
        </LinearGradient>
    )
}