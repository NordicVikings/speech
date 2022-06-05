import librosa
import fastdtw

def SimilarityAnalysis1():
    y10, sr = librosa.load("temp_audio_azure1.wav")
    y11, sr = librosa.load("temp_audio.wav")

    y10, _ = librosa.effects.trim(y10, top_db=20)
    y11, _ = librosa.effects.trim(y11, top_db=20)

    y_fast1 = librosa.effects.time_stretch(y11, rate=len(y11)/len(y10))

    mfccs10 = librosa.feature.mfcc(y=y10, sr=sr)
    mfccs11 = librosa.feature.mfcc(y=y_fast1)

    audio10 = librosa.feature.inverse.mfcc_to_mel(mfccs10)
    audio11 = librosa.feature.inverse.mfcc_to_mel(mfccs11)
    
    dist1, x1 = fastdtw.dtw(audio10, audio11, dist=20)
    return dist1


def SimilarityAnalysis2():
    y20, sr = librosa.load("temp_audio_azure2.wav")
    y21, sr = librosa.load("temp_audio.wav")

    y20, _ = librosa.effects.trim(y20, top_db=20)
    y21, _ = librosa.effects.trim(y21, top_db=20)

    y_fast2 = librosa.effects.time_stretch(y21, rate=len(y21)/len(y20))

    mfccs20 = librosa.feature.mfcc(y=y20, sr=sr)
    mfccs21 = librosa.feature.mfcc(y=y_fast2)

    audio20 = librosa.feature.inverse.mfcc_to_mel(mfccs20)
    audio21 = librosa.feature.inverse.mfcc_to_mel(mfccs21)

    dist2, x = fastdtw.fastdtw( audio20, audio21, dist=20)
    return dist2


def SimilarityAnalysis3():
    y30, sr = librosa.load("temp_audio_azure3.wav")
    y31, sr = librosa.load("temp_audio.wav")

    y30, _ = librosa.effects.trim(y30, top_db=20)
    y31, _ = librosa.effects.trim(y31, top_db=20)

    y_fast3 = librosa.effects.time_stretch(y31, rate=len(y31)/len(y30))

    mfccs30 = librosa.feature.mfcc(y=y30, sr=sr)
    mfccs31 = librosa.feature.mfcc(y=y_fast3)

    audio30 = librosa.feature.inverse.mfcc_to_mel(mfccs30)
    audio31 = librosa.feature.inverse.mfcc_to_mel(mfccs31)

    dist3, x = fastdtw.dtw( audio30, audio31, dist=20)
    return dist3
      



