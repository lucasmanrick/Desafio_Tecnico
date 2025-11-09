import { View, ScrollView, Image, TouchableOpacity, Text, ImageBackground, Alert } from "react-native";
import { style } from "./styles";
import {api} from '../../api/axios';
import {Coin} from '../../types';
import { useEffect, useState } from "react";
import ModalCripto from '../../components/modalCripto/modalCripto';
import { useNavigation, NavigationProp } from "@react-navigation/native";
import {StackParamList} from '../../types'
import { useAuth } from '../../hooks/useAuth';
import { useAuthStore } from '../../store/authStore';

export default function Home() {
    const [allCoins,setAllCoins] = useState<Coin[]>([])
    const navigation = useNavigation<NavigationProp<StackParamList,'Login'>>();
    
    const accessToken = useAuthStore((state) => state.accessToken);
    const user = useAuthStore((state) => state.user);
    const isAuthenticated = !!accessToken && !!user;

    const getAllCoins = async () =>{

        try{
            const response = await api.get<Coin[]>('/coins/')

            setAllCoins(response.data)
        }
        catch(error) {
            console.log(error)
            Alert.alert("Erro", "Nao foi possivel obter as moedas, tente novamente!")
        }
    }

    useEffect(() => {
       getAllCoins()
    },[])

    return(
    <View style={style.container}>
        <View style={style.header}>
            <Text style={style.title}>CryptoTracker</Text>
            <TouchableOpacity onPress={() => navigation.navigate("Login")}>
               {isAuthenticated ?
                (<Text style={style.textLogin}>Olá, {user?.first_name}!</Text>):
                (<Text style={style.textLogin}>Login</Text>) 
            }
            </TouchableOpacity>
        </View>
        <ScrollView contentContainerStyle={style.mainContent}>
            <View style={style.welcomeMessage}>
                <Text style={style.title}>Acompanhe e gerencie de maneira recorrente as suas moedas favoritas</Text>
            </View>
            {allCoins.map((coin:any) => (<ModalCripto key={coin.id} image={coin.image} symbol={coin.symbol} name={coin.name}/>))}
        </ScrollView>
    </View>
    )
}