import { View, ScrollView, Image, TouchableOpacity, Text, ImageBackground, Alert, FlatList, Animated } from "react-native";
import { style } from "./styles";
import { api } from '../../api/axios';
import { useEffect, useState } from "react";
import ModalCripto from '../../components/modalCripto/modalCripto';
import { useNavigation, NavigationProp } from "@react-navigation/native";
import { StackParamList, Coin } from '../../types'
import { useAuth } from '../../hooks/useAuth';
import { Ionicons } from '@expo/vector-icons';


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

        }
        catch (error) {
            console.log(error)
            Alert.alert("Erro", "Nao foi possivel obter as moedas, tente novamente!")
        }
    }

    useEffect(() => {
        getCoins()
        if (visibleCoins.length === 0) {
            setVisibleCoins(allCoins.slice(0, itemsPerPage));
        }
    }, [])

    // useEffect(() => {  // se for requisitar moedas por pagina, direto do back end
    //     getCoins()
    // }, [page])

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
                renderItem={({ item }) => <ModalCripto id={item.id} image={item.image} symbol={item.symbol} name={item.name} homepage="S" />}
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