public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        System.out.println(d(">JÂ0ûDwù¯0Õ´zhÝ!ë\u000ff", -989022505));
        System.out.println(d(">JÂ0ûDwù¯0Õ´zhÝ!ë\u000ff", -989022505));
        System.out.println(d("rî:MGì0BSvn", -2055632580));
        System.out.println(d("+À0­0G¤nò\r3È6", 675347394));
        System.out.println(d("QLÜkh^F,j_È\u0015%Yî Oukd", -1263812037));
        System.out.println(d("zè3`y§&QiquL>ú5db§\u0016FssdW[ì<Rqì&", -451507951));
        System.out.println(d("KË", -867135215));
        System.out.println(d(":È1¥4Å½jð\"À7", 336766939));
        System.out.println(d("\u0005fã", -930415931));
        System.out.println(d("obVpûlcsþ0U~+pPtàlIw×!SphfTtñ\u0011pdä", -768401274));
        System.out.println(d("\u000eé", 194738646));
        System.out.println(d("*À§ {2[;põ\u0006nâ¸1kÅ#", -822830269));
        System.out.println(d("\u0014lþ\u0007ú(AT¿\u001fí\u001a", 1548356339));
        System.out.println(d(";È!aq6Ù uwÅê>paÈ'", 370203992));
        System.out.println(d("lmiu", 1209022468));
        System.out.println(d(";È)e\u0005Ð4Å\u001c:BÀ%Ì8aY", -341371526));
        System.out.println(d("AR|P", 1490185396));
        System.out.println(d("kà\u0017p¯²$Bô3HEx¯*tø", -1361421952));
        System.out.println(d("nbÞ4 ebÑ#À!}-Û%Ä0.@È6Æ'mwÀ8ñ2r`É4Ý0vPØ0Â", -702764379));
        System.out.println(d("jú$Y5gqLaý(;Hå5I~v", 1547207220));
        System.out.println(d("0Dpyå\u000fx", 148803807));
        System.out.println(d("NI", -1487124972));
    }

    public static int INTGET=1;

    public static char a(char c, int i) {
        return (char) (c & ((1 << i) ^ 65535));
    }
    public static char b(char c, int i) {
        return (char) (c | (1 << i));
    }
    public static char c(char c, int i) {
        return (char) ((c & (1 << i)) >> i);
    }
    public static String d(CharSequence charSequence, int i) {
        StringBuilder sb = new StringBuilder();
        if (i == 0) {
            return sb.toString();
        }
        for (int i2 = 0; i2 < charSequence.length(); i2++) {
            char charAt = charSequence.charAt(i2);
            char c = (char) (i >> (i2 % 4));
            int i3 = i2 % 3;
            if (i3 == 0) {
                for (int i4 = 0; i4 < 8; i4 += 2) {
                    char c2 = (char) (c(charAt, i4) ^ c(c, i4));
                    if (c2 == 0) {
                        charAt = a(charAt, i4);
                    } else if (c2 == 1) {
                        charAt = b(charAt, i4);
                    }
                }
            } else if (i3 == 1) {
                for (int i5 = 1; i5 < 8; i5 += 2) {
                    char c3 = (char) (c(charAt, i5) ^ c(c, i5));
                    if (c3 == 0) {
                        charAt = a(charAt, i5);
                    } else if (c3 == 1) {
                        charAt = b(charAt, i5);
                    }
                }
            } else if (i3 == 2) {
                for (int i6 = 0; i6 < 8; i6++) {
                    char c4 = (char) (c(charAt, i6) ^ c(c, i6));
                    if (c4 == 0) {
                        charAt = a(charAt, i6);
                    } else if (c4 == 1) {
                        charAt = b(charAt, i6);
                    }
                }
            }
            sb.append((char) (charAt ^ INTGET));
        }
        return sb.toString();
    }
}