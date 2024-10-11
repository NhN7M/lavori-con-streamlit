import streamlit as st

class Orario:
    
    def __init__(self):
        self.lunes = {
            '1ra': 'angles',
            '2na': 'alemany',
            '3ra': 'matematiques',
            '4ta': 'plastica',
            '5ta': 'F.Q.',
            '6ta': 'tutoria'
        }
        self.martes = {
            '1ra': 'tecnologia',
            '2na': 'G.H.',
            '3ra': 'F.Q.',
            '4ta': 'matematiques',
            '5ta': 'plastica',
            '6ta': 'castellà'
        }
        self.miercoles = {
            '1ra': 'G.H.',
            '2na': 'tecnologia',
            '3ra': 'català',
            '4ta': 'F.Q.',
            '5ta': 'castellà',
            '6ta': 'angles'
        }
        self.jueves = {
            '1ra': 'matematiques',
            '2na': 'A.E.',
            '3ra': 'castellà',
            '4ta': 'E.F.',
            '5ta': 'català',
            '6ta': 'alemany'
        }
        self.viernes = {
            '1ra': 'G.H.',
            '2na': 'català',
            '3ra': 'E.F.',
            '4ta': 'angles',
            '5ta': 'tecnologia',
            '6ta': 'plastica'
        }

    st.title('Horario de escuela')
    st.subheader('Que asignatura tengo?')


    def ora(self):
        dia = st.selectbox(
        'Elije un dia de la semana',
        ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
        )
        
        if dia == 'lunes':
            hora =st.selectbox(
            'Selecciona un horario',
            ['1ra', '2na', '3ra', '4ta', '5ta', '6ta']
            )
            if hora == '1ra':
                st.info(self.lunes['1ra'])
            elif hora == '2na':
                st.info(self.lunes['2na'])
            elif hora == '3ra':
                st.info(self.lunes['3ra'])
            elif hora == '4ta':
                st.info(self.lunes['4ta'])
            elif hora == '5ta':
                st.info(self.lunes['5ta'])
            elif hora == '6ta':
                st.info(self.lunes['6ta'])
            else:
                st.error('hora no valida')
        elif dia == 'martes':
            hora = st.selectbox(
                'Selecciona un horario',
                ['1ra', '2na', '3ra', '4ta', '5ta', '6ta']
            )
            if hora == '1ra':
                st.info(self.martes['1ra'])
            elif hora == '2na':
                st.info(self.martes['2na'])
            elif hora == '3ra':
                st.info(self.martes['3ra'])
            elif hora == '4ta':
                st.info(self.martes['4ta'])
            elif hora == '5ta':
                st.info(self.martes['5ta'])
            elif hora == '6ta':
                st.info(self.martes['6ta'])
            else:
                st.error('hora no valida')
        elif dia == 'miercoles':
            hora = st.selectbox(
                'Selecciona un horario',
                ['1ra', '2na', '3ra', '4ta', '5ta', '6ta']
            )
            if hora == '1ra':
                st.info(self.miercoles['1ra'])
            elif hora == '2na':
                st.info(self.miercoles['2na'])
            elif hora == '3ra':
                st.info(self.miercoles['3ra'])
            elif hora == '4ta':
                st.info(self.miercoles['4ta'])
            elif hora == '5ta':
                st.info(self.miercoles['5ta'])
            elif hora == '6ta':
                st.info(self.miercoles['6ta'])
            else:
                st.error('hora no valida')
        elif dia == 'jueves':
            hora = st.selectbox(
                'Selecciona un horario',
                ['1ra', '2na', '3ra', '4ta', '5ta', '6ta']
            )
            if hora == '1ra':
                st.info(self.jueves['1ra'])
            elif hora == '2na':
                st.info(self.jueves['2na'])
            elif hora == '3ra':
                st.info(self.jueves['3ra'])
            elif hora == '4ta':
                st.info(self.jueves['4ta'])
            elif hora == '5ta':
                st.info(self.jueves['5ta'])
            elif hora == '6ta':
                st.info(self.jueves['6ta'])
            else:
                st.error('hora no valida')
        elif dia == 'viernes':
            hora = st.selectbox(
                'Selecciona un horario',
                ['1ra', '2na', '3ra', '4ta', '5ta', '6ta']
            )
            if hora == '1ra':
                st.info(self.viernes['1ra'])
            elif hora == '2na':
                st.info(self.viernes['2na'])
            elif hora == '3ra':
                st.info(self.viernes['3ra'])
            elif hora == '4ta':
                st.info(self.viernes['4ta'])
            elif hora == '5ta':
                st.info(self.viernes['5ta'])
            elif hora == '6ta':
                st.info(self.viernes['6ta'])
            else:
                st.error('hora no valida')
        else:
            print('este dia no hay cole')
                
            
horario = Orario()
horario.ora()
    
