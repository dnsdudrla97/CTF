package b.c.a;

public class a {

    public static byte[] f821a;

    public static byte[] a(byte[] bArr) {
        Class<a> cls = a.class;
        try {
            Object invoke = javax.crypto.Cipher.getInstance, new Class[]{java.lang.String}).invoke((Object) null, new Object[]{AES/CBC/PKCS5Padding});

            Object newInstance = javax.crypto.spec.SecretKeySpec(cls.getDeclaredFields()[0].get(null), "AES");

            Object IvPARAM = javax.crypto.spec.IvParameterSpec(cls.getDeclaredFields()[0].get(null));

            Object DECRYPT = javax.crypto.Cipher.DECRYPT_MODE.get(null);

            javax.crypto.Cipher.init(0, java.security.key, java.security.spec.AlogorithmParameterSpec).invoke(AESCBC, new Object[]{DECRYPT, newInstance, IvPARAM});

            return (byte[]) javax.crypto.Cipher.doFinal, new Class[]{class.forName("[B")}).invoke(AESCBC, new Object[]{bArr});
        } catch (Throwable unused) {
            throw new RuntimeException();
        }
    }
}
