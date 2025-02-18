import streamlit as st

class P1:

    def __init__(self):
        self.deb_p1 = 0

    def debito_1(self, deb_p1=None):
        piu_1 = float(st.text_input('quanti soldi devi: '))
        self.deb_p1 = float(self.deb_p1 + piu_1)

    def dati_1(self, deb_p1=None):
        meno_1 = float(st.number_input('quanti soldi hai dato: '))
        self.deb_p1 = float(self.deb_p1 - meno_1)

    def mostra(self):
        st.info(self.deb_p1)


class P2:

    def __init__(self):
        self.deb_p2 = 0

    def debito_2(self, deb_p2=None):
        piu_2 = float(st.number_input('quanti soldi devi: '))
        self.deb_p2 = float(self.deb_p2 + piu_2)

    def dati_2(self, deb_p2=None):
        meno_2 = float(st.number_input('quanti soldi hai dato: '))
        self.deb_p2 = float(self.deb_p2 - meno_2)

    def mostra(self):
        st.info(self.deb_p2)

P1 = P1()
P2 = P2()

def main():
    st.title('Conta soldi')
    st.subheader('Benvenuto nel tuo conta soldi')

    st.text('p1')
    azione = st.selectbox(
        'Devi aggiungere o diminuire il tuo debito: ',
        ['aggiungere', 'diminuire']
        ).lower()
    if azione == 'aggiungere':
        P2.debito_2()
    elif azione == 'diminuire':
        P2.dati_2()
    else:
        st.warning('risposta non accettata')
    P2.mostra()

    st.text('p2')
    azione = st.selectbox(
        'devi aggiungere o diminuire il tuo debito: ',
        ['aggiungere', 'diminuire']
        ).lower()
    if azione == 'aggiungere':
        P1.debito_1()
    elif azione == 'diminuire':
        P1.dati_1()
    else:
        st.warning('risposta non accettata')
    P1.mostra()



if __name__ == '__main__':
    main()