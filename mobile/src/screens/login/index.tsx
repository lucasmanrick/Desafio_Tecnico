import React, { useState } from "react";

import {Text, View, TextInput, TouchableOpacity, Alert } from 'react-native';
import {style} from './styles';
import { LinearGradient } from 'expo-linear-gradient';
import {api} from '../../api/axios';
import { LoginRequest, LoginResponse, RegisterRequest, RegisterResponse } from '../../types';
import { useAuthStore } from "../../store/authStore";


export default function login(){
    const [email,setEmail] = useState('')
    const [password,setPassword] = useState('')
    const [firstName,setFirstName] = useState('')
    const [lastName,setLastName] = useState('')
    const [registerTime, setRegisterTime] = useState('N')

    const loginStore = useAuthStore((state) => state.login);
    const sendLogin = async () => {
        console.log("clicou")
        if(email === '' || password === '') {
            Alert.alert("Atenção", "Preencha todos os campos antes de tentar logar!");
            return
        }
        
        const payload: LoginRequest = {email,password}
        
        try {
        console.log("iniciando requisição")
        const response = await api.post<LoginResponse>('/auth/login/',payload);


        loginStore(response.data)

        registerTime === 'N' ? Alert.alert("Sucesso", "Login efetuado com sucesso!") : ''
        console.log(`usuario logado com sucesso: ${response.data.user}`)
    }
    catch (error) {
        console.log(error)
        if(registerTime === 'N') {
        Alert.alert("Erro", "Erro ao tentar efetuar login!")}
        else{
            setRegisterTime('N')
        }
    }

    };


    const tryRegister = async () => {
        if(firstName === '' || lastName === '' || email === '' || password === '') {
            Alert.alert("Atencao", "Preencha todos os campos antes de registrar-se!")
            return
        }

        try{
            const payload:RegisterRequest = {email,password,first_name:firstName,last_name:lastName}

            const response = await api.post<RegisterResponse>('/auth/register/',payload);

            sendLogin(); //se der certo a pessoa se registrar já faz o login dela.

            Alert.alert("Sucesso", "Registro efetuado com sucesso!")
        }
        catch(error){
            Alert.alert("Erro", "Não foi possivel se registrar, tente novamente!")
        }
    }


    return(
        <LinearGradient 
        colors={['#000000ff','#000a70ff']} // cores do gradiente
        start={{ x: 1, y: 0.5 }}
        end={{ x: 1, y: 0 }}
        style={style.container}>
            <View style={style.header}>
                <Text style={style.title}>CryptoTracker</Text>
            </View>
            <View style={style.mainContent}>
                {registerTime === 'N' ? (
                <>
                    <Text style={style.text}>email:</Text>
                    <TextInput style={style.inputStyle} onChangeText={setEmail}/>
                    <Text style={style.text}>password:</Text>
                    <TextInput style={style.inputStyle} onChangeText={setPassword}/>
                    <View style={style.buttonContainer}>
                        <TouchableOpacity   
                        onPress={sendLogin} 
                        style={style.button}>
                            <Text style={style.buttonText}>Entrar</Text>
                        </TouchableOpacity>
                        <TouchableOpacity onPress={() => setRegisterTime('S')}>
                            <Text style={style.text}>Registrar-se</Text>
                        </TouchableOpacity>
                    </View>
                </>
                ): (
                     <>
                    <Text style={style.text}>email:</Text>
                    <TextInput style={style.inputStyle} onChangeText={(text) => setEmail(text)}/>
                    <Text style={style.text}>senha:</Text>
                    <TextInput style={style.inputStyle} onChangeText={(text) => setPassword(text)}/>
                    <Text style={style.text}>primeiro nome:</Text>
                    <TextInput style={style.inputStyle} onChangeText={(text) => setFirstName(text)}/>
                    <Text style={style.text}>sobrenome:</Text>
                    <TextInput style={style.inputStyle} onChangeText={(text) => setLastName(text)}/>
                    <View style={style.buttonContainer}>
                        <TouchableOpacity   
                        onPress={tryRegister} 
                        style={style.button}>
                            <Text style={style.buttonText}>Registrar-se</Text>
                        </TouchableOpacity>
                        <TouchableOpacity onPress={() => setRegisterTime('N')}>
                            <Text style={style.text}>Já possuo uma conta</Text>
                        </TouchableOpacity>
                    </View>
                </>
                )}
            </View>

        </LinearGradient>
    )
}