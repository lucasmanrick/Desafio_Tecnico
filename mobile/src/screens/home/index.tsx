import { View, ScrollView, Image, TouchableOpacity, Text, ImageBackground, Alert, FlatList, Animated } from "react-native";
import { useEffect, useState, useCallback, use } from "react";
import { useFocusEffect } from '@react-navigation/native';
import { useNavigation, NavigationProp } from "@react-navigation/native";
import { Ionicons } from '@expo/vector-icons';

// imports do proprio projeto
import { style } from "./styles";
import { api } from '../../api/axios';
import ModalCripto from '../../components/modalCripto/modalCripto';
import { StackParamList, Coin } from '../../types'
import { useAuth } from '../../hooks/useAuth';


export default function Home() {
    const navigation = useNavigation<NavigationProp<StackParamList, 'Login'>>();
    const { isAuthenticated, user, logout } = useAuth();

    //paginação das 100 moedas no front end
    const [allCoins, setAllCoins] = useState<Coin[]>([])
    const [visibleCoins, setVisibleCoins] = useState<Coin[]>([]);
    const [itemsPerPage, setItemsPerPage] = useState(20);
    const [loading, setLoading] = useState(false);




    const loadMoreCoins = () => {
        const nextItems = allCoins.slice(visibleCoins.length, visibleCoins.length + itemsPerPage);
        setVisibleCoins([...visibleCoins, ...nextItems]);

        if (nextItems.length < itemsPerPage) {
            setLoading(false);
        }
    };


    const getCoins = async () => {

        try {
            const response = await api.get<Coin[]>(`/coins/?per_page=100&page=1`)
            setAllCoins(response.data)
             // se for a primeira requisição das moedas (assim que abre a pagina ou volta pra ela, nós passamos visiblecoins para 0 e carregamos 20 moedas novamente) 
            setVisibleCoins(response.data.slice(0, itemsPerPage));
            

            
        }
        catch (error) {
            console.log(error)
            Alert.alert("Erro", "Nao foi possivel obter as moedas, tente novamente!")
        }
    }


    useFocusEffect(
        useCallback(() => {
            setAllCoins([])
            getCoins();
        }, [])
    );


    // useEffect(() => {
    //     getCoins()
    // }, []);

    return (
        <View style={style.container}>
            <View style={style.header}>
                <Text style={style.title}>CryptoTracker</Text>
                {isAuthenticated ? (<Text style={style.textLogin}>Olá, {user?.first_name}!</Text>) :
                    (
                        <TouchableOpacity onPress={() => navigation.navigate("Login")}>
                            <Text style={style.textLogin}>Login</Text>
                        </TouchableOpacity>)
                }

            </View>

            <FlatList
                data={visibleCoins}
                renderItem={({ item }) => <ModalCripto id={item.id} currentPrice={item.current_price} image={item.image} symbol={item.symbol} name={item.name} homepage="S" />}
                keyExtractor={(item) => item.id}
                ListHeaderComponent={
                    <View style={style.welcomeMessage}>
                        <Text style={style.title}>
                            Acompanhe e gerencie de maneira recorrente as suas moedas favoritas
                        </Text>
                    </View>}
                onEndReached={() => { loadMoreCoins(); setLoading(true) }}
            />


            {
                isAuthenticated ? (
                    <TouchableOpacity style={style.quitButton} onPress={() => {
                        logout();
                        navigation.navigate('Login')
                    }}>
                        <Ionicons name="exit-outline" size={30} color="white" />
                    </TouchableOpacity>) : ''
            }
        </View>
    )
}