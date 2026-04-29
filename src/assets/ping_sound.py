import streamlit as st
import streamlit.components.v1 as components
def play_ping_sound():
    try:
        # Option 1: local file (put your own ping.mp3 in assets/)
        ping_file = "assets/ping.mp3"
        with open(ping_file, "rb") as f:
            audio_bytes = f.read()
        st.audio(audio_bytes, format="audio/mpeg", autoplay=True)
    except FileNotFoundError:
        # Option 2: fallback – Web Audio beep (works after user click)
        components.html("""
            <script>
                (function() {
                    try {
                        var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                        var oscillator = audioCtx.createOscillator();
                        var gainNode = audioCtx.createGain();
                        oscillator.connect(gainNode);
                        gainNode.connect(audioCtx.destination);
                        oscillator.frequency.value = 880;   // high 'ping' tone
                        gainNode.gain.value = 0.2;
                        oscillator.type = 'sine';
                        oscillator.start();
                        gainNode.gain.exponentialRampToValueAtTime(0.00001, audioCtx.currentTime + 0.3);
                        oscillator.stop(audioCtx.currentTime + 0.3);
                        audioCtx.resume();
                    } catch(e) {
                        console.log("Web Audio not supported – add a custom ping.mp3 to assets/");
                    }
                })();
            </script>
        """, height=0)
    except Exception:
        # Silent fail – no sound
        pass