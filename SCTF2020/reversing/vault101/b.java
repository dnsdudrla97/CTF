package b.c.a;

import android.os.Binder;
import android.os.IBinder;
import android.os.IInterface;
import android.os.Parcel;

public interface b extends IInterface {

    public static abstract class a extends Binder implements b {

        /* renamed from: b.c.a.b$a$a  reason: collision with other inner class name */
        public static class C0039a implements b {

            /* renamed from: a  reason: collision with root package name */
            public IBinder f822a;

            public C0039a(IBinder iBinder) {
                this.f822a = iBinder;
            }

            public boolean a(String str) {
                Parcel obtain = Parcel.obtain();
                Parcel obtain2 = Parcel.obtain();
                try {
                    obtain.writeInterfaceToken("com.sctf2020.vault101.IVault");
                    obtain.writeString(str);
                    boolean z = false;
                    this.f822a.transact(1, obtain, obtain2, 0);
                    obtain2.readException();
                    if (obtain2.readInt() != 0) {
                        z = true;
                    }
                    return z;
                } finally {
                    obtain2.recycle();
                    obtain.recycle();
                }
            }

            public IBinder asBinder() {
                return this.f822a;
            }
        }

        public a() {
            attachInterface(this, "com.sctf2020.vault101.IVault");
        }

        public static b b(IBinder iBinder) {
            if (iBinder == null) {
                return null;
            }
            IInterface queryLocalInterface = iBinder.queryLocalInterface("com.sctf2020.vault101.IVault");
            return (queryLocalInterface == null || !(queryLocalInterface instanceof b)) ? new C0039a(iBinder) : (b) queryLocalInterface;
        }

        public IBinder asBinder() {
            return this;
        }

        public boolean onTransact(int i, Parcel parcel, Parcel parcel2, int i2) {
            if (i == 1) {
                parcel.enforceInterface("com.sctf2020.vault101.IVault");
                boolean a2 = a(parcel.readString());
                parcel2.writeNoException();
                parcel2.writeInt(a2 ? 1 : 0);
                return true;
            } else if (i != 1598968902) {
                return super.onTransact(i, parcel, parcel2, i2);
            } else {
                parcel2.writeString("com.sctf2020.vault101.IVault");
                return true;
            }
        }
    }

    boolean a(String str);
}